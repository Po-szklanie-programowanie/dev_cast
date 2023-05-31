import subprocess
import time

def check_container_running(container_name):
    cmd = f"docker compose ps {container_name}"
    output = subprocess.check_output(cmd, shell=True, text=True)
    return "Up" in output

def wait_for_container(container_name):
    while not check_container_running(container_name):
        time.sleep(5)

def run_container(container_name):
    cmd = f"docker compose up -d {container_name}"
    subprocess.run(cmd, shell=True)

def run_containers_in_order(container_list):
    for container in container_list:
        run_container(container)
        wait_for_container(container)

def build_docker_images():
    cmd = "docker compose build"
    subprocess.run(cmd, shell=True)

# Lista kontenerów w kolejności uruchamiania
containers = ["db", "pgadmin4", "icecast2", "ffmpeg-lofi",
               "ffmpeg-phonk", "backend", "frontend"]
build_docker_images()
run_containers_in_order(containers)