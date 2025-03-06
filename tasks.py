from invoke import task


@task
def up(c):
    c.run("docker compose up -d --build")


@task
def b(c):
    c.run("black .")


@task
def makemigrations(c):
    c.run("python manage.py makemigrations")


@task(pre=[makemigrations])
def m(c):
    c.run("python manage.py migrate")

    print("运行迁移命令")
