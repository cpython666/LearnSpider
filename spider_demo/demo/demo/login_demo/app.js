const TX = new TextEncoder();
function toBytes(s){return TX.encode(s)}
function toBase64(arr){return btoa(String.fromCharCode.apply(null, Array.from(arr)))}
function rotr(n,x){return (x>>>n)|(x<<(32-n))}
function sha256(bytes){
  const H=[0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19];
  const K=[0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2];
  const l=bytes.length;
  const ml=l*8;
  const withOne=Uint8Array.from([...bytes,0x80]);
  let zlen=((withOne.length+8+64)>>6<<6); 
  if(zlen-withOne.length<8) zlen+=64;
  const buf=new Uint8Array(zlen);
  buf.set(withOne);
  const dv=new DataView(buf.buffer);
  dv.setUint32(buf.length-4, ml>>>0);
  dv.setUint32(buf.length-8, Math.floor(ml/0x100000000));
  for(let i=0;i<buf.length;i+=64){
    const w=new Uint32Array(64);
    for(let j=0;j<16;j++){w[j]=dv.getUint32(i+j*4);}
    for(let j=16;j<64;j++){
      const s0=rotr(7,w[j-15])^rotr(18,w[j-15])^(w[j-15]>>>3);
      const s1=rotr(17,w[j-2])^rotr(19,w[j-2])^(w[j-2]>>>10);
      w[j]=(w[j-16]+s0+w[j-7]+s1)>>>0;
    }
    let a=H[0],b=H[1],c=H[2],d=H[3],e=H[4],f=H[5],g=H[6],h=H[7];
    for(let j=0;j<64;j++){
      const S1=rotr(6,e)^rotr(11,e)^rotr(25,e);
      const ch=(e&f)^(~e&g);
      const t1=(h+S1+ch+K[j]+w[j])>>>0;
      const S0=rotr(2,a)^rotr(13,a)^rotr(22,a);
      const maj=(a&b)^(a&c)^(b&c);
      const t2=(S0+maj)>>>0;
      h=g;g=f;f=e;e=(d+t1)>>>0;d=c;c=b;b=a;a=(t1+t2)>>>0;
    }
    H[0]=(H[0]+a)>>>0;H[1]=(H[1]+b)>>>0;H[2]=(H[2]+c)>>>0;H[3]=(H[3]+d)>>>0;H[4]=(H[4]+e)>>>0;H[5]=(H[5]+f)>>>0;H[6]=(H[6]+g)>>>0;H[7]=(H[7]+h)>>>0;
  }
  const out=new Uint8Array(32);
  const outdv=new DataView(out.buffer);
  for(let i=0;i<8;i++){outdv.setUint32(i*4,H[i]);}
  return out;
}
function hmacSha256(key,msg){
  const block=64;
  let k=key;
  if(k.length>block) k=sha256(k);
  if(k.length<block){const kk=new Uint8Array(block);kk.set(k);k=kk;}
  const o=new Uint8Array(block), i=new Uint8Array(block);
  for(let idx=0;idx<block;idx++){o[idx]=k[idx]^0x5c;i[idx]=k[idx]^0x36;}
  const inner=new Uint8Array(i.length+msg.length);
  inner.set(i);inner.set(msg,i.length);
  const innerHash=sha256(inner);
  const outer=new Uint8Array(o.length+innerHash.length);
  outer.set(o);outer.set(innerHash,o.length);
  return sha256(outer);
}
function pbkdf2Sha256(password,salt,iterations,dkLen){
  const hLen=32;const l=Math.ceil(dkLen/hLen);const r=dkLen-(l-1)*hLen;
  const DK=new Uint8Array(dkLen);
  for(let i=1;i<=l;i++){
    const INT_i=new Uint8Array([0,0,0,i]);
    let U=hmacSha256(password, new Uint8Array([...salt,...INT_i]));
    let T=U.slice();
    for(let j=1;j<iterations;j++){
      U=hmacSha256(password,U);
      for(let k=0;k<hLen;k++){T[k]^=U[k];}
    }
    const start=(i-1)*hLen;
    const len=(i===l)?r:hLen;
    DK.set(T.slice(0,len), start);
  }
  return DK;
}
function deriveTokenSync(pwd){
  const salt=document.querySelector('meta[name="login-salt"]').content;
  const secret=document.querySelector('meta[name="login-secret"]').content;
  const pepper=document.querySelector('meta[name="login-pepper"]').content;
  const key=pbkdf2Sha256(toBytes(pwd), toBytes(salt), 200000, 32);
  const mac=hmacSha256(key, toBytes(secret+pepper));
  return toBase64(mac);
}
const go = document.getElementById("go"),
  pwd = document.getElementById("pwd"),
  msg = document.getElementById("msg");
go.addEventListener("click", async () => {
  go.disabled = true;
  msg.textContent = "";
  try {
    const token = deriveTokenSync(pwd.value);
    const r = await fetch("http://localhost:8091/api/login", {
      method: "POST",
      headers: { "X-Client-Auth": token },
    });
    const j = await r.json();
    if (j && j.ok) {
      msg.textContent = "Login success";
      msg.className = "msg ok";
    } else {
      msg.textContent = "Invalid password";
      msg.className = "msg err";
    }
  } catch (err) {
    msg.textContent = "Error";
    msg.className = "msg err";
  } finally {
    go.disabled = false;
  }
});
