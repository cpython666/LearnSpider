<h1 align="center">爬虫百战成神 (LearnSpider)</h1>
<p align="center">
<a href="https://space.bilibili.com/1909782963">
<img src="./static/imgs/logo.jpeg" alt="StarDreamSpider" width="300" />
</a>
</p>
<p align="center"><b>来一场爬虫与成神相结合的旅行吧！</b></p>

## 项目介绍

爬虫百战成神（LearnSpider）是一个面向初学者到高级用户的爬虫练习网站。我们提供了多种技术示例代码、详细的文档讲解和视频演示，帮助用户从零开始学习并掌握爬虫技术。

## 详细介绍

这是一个使用django+drf做一个爬虫刷题网站，也就是一个靶场，我创建这个项目的代码仓库名为LearnSpider，中文叫：爬虫百战成神。

它不仅是一个练习场，也配套有每道题目的多种技术示例代码，文档讲解，视频演示。题目由易到难，由浅入深，想让大家在刷题与实践的过程中甚至是从零学会爬虫（因为思想学会后，剩下的代码其实就是工具的使用），在这个过程中增加自己对于代码和场景的理解。本项目目标覆盖爬虫初级，进阶和高级。涉及到requests，scrapy这些请求工具，还有selenium，drissionpage这些自动化工具框架。涉及到接口请求，静态页面解析，也涉及到代码混淆，接口加密，也包含各种抓包工具的使用，chrome开发者工具的使用等。包括一些新颖的反爬技术，比如前端层面的反爬，svg反爬，css反爬，雪碧图等，也比如新兴的反爬技术比如wasm，总之就是我会什么，就像教大家什么。所以此仓库的内容也会无限拓展。也欢迎大家的贡献。

此仓库旨在让大家在刷题的过程中以结果和成就感驱动学习，学习到某个知识点后可以快速应用，从而感受到学到了东西，爬虫是如此的简单有趣。而不是学完之后因为网站内容变动而没有刷题的地方，久而久之像没学一样。并且本项目最想让大家养成举一反三，逻辑推理的思考思维习惯。

搭建此项目使用的技术栈是Django+DRF+JQuery。使用django的模板语法实现前端，使用jquery实现页面js逻辑与请求，drf实现请求限流。数据库使用sqlite。前端样式实现使用的bootstrap，本来想着手搓的，后面做的时候有感觉没必要给自己增加无意义的工作量。
### 项目目标

- **覆盖范围**：从初级到高级的爬虫技术
- **工具与框架**：requests、scrapy、selenium、drissionpage等
- **技术点**：
  - 接口请求与静态页面解析
  - 代码混淆与接口加密
  - 各种抓包工具与Chrome开发者工具使用
  - 新颖的反爬技术（前端层面、SVG、CSS、雪碧图、WASM等）

### 项目特色

1. **全面覆盖**：包含从入门到高级的各类爬虫技术与工具使用。
2. **示例丰富**：每道题目提供多种技术示例代码。
3. **详细讲解**：文档与视频讲解，帮助理解每个技术点。
4. **持续更新**：内容会随着新技术的出现不断扩展。
5. **社区贡献**：欢迎大家贡献自己的题目和解法。

### 学习方式

- 通过刷题和实践，从零开始学习爬虫技术。
- 以结果和成就感驱动学习，快速应用所学知识。
- 培养举一反三和逻辑推理的思维习惯。

## 账号密码
LearnSpider
LearnSpider
邮箱：cpython666@gmail.com
## 技术栈

- 后端框架：Django + Django REST Framework (DRF)
- 前端：使用Django模板语法

## 项目结构

```plaintext
LearnSpider/
├── backend/        # 后端代码
├── frontend/       # 前端代码
├── templates/      # Django 模板文件
├── static/         # 静态文件
├── docs/           # 项目文档
├── videos/         # 视频演示
└── README.md       # 项目说明
```

## 安装与运行

### 环境要求

- Python 3.11+
- Django 4.2+
- Django REST Framework

### 安装步骤

1. 克隆项目代码：

   ```bash
   git clone https://github.com/你的用户名/LearnSpider.git
   cd LearnSpider
   ```

2. 创建并激活虚拟环境：

   ```bash
   python -m venv venv
   source venv/bin/activate  # 对于Windows用户：venv\Scripts\activate
   ```

3. 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```

4. 运行数据库迁移：

   ```bash
   python manage.py migrate
   ```

5. 启动开发服务器：

   ```bash
   python manage.py runserver
   ```

6. 在浏览器中打开 `http://127.0.0.1:8000` 查看项目。

## 贡献指南

1. Fork 本仓库
2. 创建一个新的分支 (`git checkout -b feature/你的特性`)
3. 提交你的更改 (`git commit -am '添加了新的功能'`)
4. 推送到分支 (`git push origin feature/你的特性`)
5. 创建一个新的 Pull Request

## 联系我们

如有任何问题或建议，请通过以下方式联系我们：

- Email: 你的邮箱@example.com
- GitHub Issues: https://github.com/你的用户名/LearnSpider/issues

---

### 建议

1. **用户体验优化**：虽然前端使用Django模板语法，但可以考虑引入一些现代的前端库和框架，如Bootstrap或Tailwind CSS，以提升用户体验。
2. **单元测试与持续集成**：增加单元测试，使用CI工具如Travis CI或GitHub Actions，确保代码质量。
3. **文档与教程**：持续完善文档，增加更多详细的教程和示例代码，帮助用户更好地理解和应用技术。
4. **社区互动**：建立一个论坛或使用GitHub Discussions，促进用户间的交流与分享。
5. **安全性与性能优化**：关注爬虫的安全性，避免被反爬机制检测，并优化性能，提升爬取效率。

希望这些建议对你的项目有所帮助！如果有更多问题，随时联系我。

**注意：** 该项目仅供学习和交流使用，不得用于非法活动。作者对任何滥用项目所导致的问题概不负责。

根据难度分数计算显示顺序
```bash
python manage.py update_order_ids
python manage.py update_pass_status
```
```bash

```