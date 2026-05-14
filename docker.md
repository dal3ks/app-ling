# Docker 

## Key commands

| Command | What it does |
| `docker run -d <image>` | Run a container in the background (detached) |
| `docker ps` | List all running containers |
| `docker stop <container_id>` | Stop a running container |
| `docker attach <container_id>` | Connect to a running container |
| `docker volume create <name>` | Create a volume to persist data |

## Key concepts from investigations

**Containers don't persist data by default**
If you save a file inside a container, stop it, and restart it — the file is gone. Use volumes to persist data beyond the lifecycle of a container.

**Volumes**
Volumes live outside the container. Critical for stateful apps like databases — without a volume, every PostgreSQL restart would wipe your data.

```bash
docker volume create log-data
```

**Docker images are like a venv on steroids**
A venv packages Python dependencies. A Docker image packages everything — the OS, system libraries, drivers, and app dependencies. Pull the image and it just works, no setup needed.

**Dev containers**
A VS Code Dev Container runs your entire development environment inside Docker. Every developer on a team gets the exact same setup — no "works on my machine" problems. This is development environment as code.

**Architecture and Docker**
Not all programs run on all computers because of different CPU architectures (ARM vs x86) and OS differences. Docker solves the dependency problem by bundling everything in an image. It partially solves the architecture problem via emulation, but a Linux container still needs a Linux kernel — which is why Docker Desktop on Mac runs a hidden Linux VM behind the scenes.

