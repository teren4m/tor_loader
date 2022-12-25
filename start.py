import subprocess as sb


def run(comand, *arrgs):
    data = [comand]
    data.extend(arrgs)
    sb.run(data)


def build_docker(name):
    run(
        "docker",
        "build",
        "-t",
        name,
        ".")

def clear_docker_all():
    run(
        "docker",
        "system",
        "prune",
        "-a",
        "-f",
    )

def clear_docker_containers():
    run(
        "docker",
        "rm",
        "$(docker ps -a -q)"
    )

def stop_docker_container(name):
    run(
        "docker",
        "stop",
        name,
    )

app_name = "tor_proxy"

stop_docker_container(app_name)
clear_docker_all()
build_docker(app_name)

# docker run -d -p 80:5000 --name=tor_proxy tor_proxy
