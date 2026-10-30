# Docker Setup Guide

This guide covers installing Docker on Linux, macOS, and Windows. On macOS and Windows, install **Docker Desktop**; on Linux, install **Docker Engine** from Docker's official package repository.

## Linux

The commands below install Docker Engine on Ubuntu. For other distributions, including Debian, Fedora, and RHEL, follow the [official Docker Engine installation guide](https://docs.docker.com/engine/install/) and select your distribution.

### Ubuntu

1. Remove conflicting or older packages, if installed:

   ```bash
   sudo apt-get remove docker.io docker-doc docker-compose podman-docker containerd runc
   ```

2. Add Docker's official APT repository:

   ```bash
   sudo apt-get update
   sudo apt-get install ca-certificates curl
   sudo install -m 0755 -d /etc/apt/keyrings
   sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
     -o /etc/apt/keyrings/docker.asc
   sudo chmod a+r /etc/apt/keyrings/docker.asc

   echo \
     "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
     $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
     sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   ```

3. Install Docker Engine and its plugins:

   ```bash
   sudo apt-get update
   sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
   ```

4. Verify the installation:

   ```bash
   sudo docker run --rm hello-world
   ```

Docker starts automatically on most Ubuntu installations. To check or start the service:

```bash
sudo systemctl status docker
sudo systemctl start docker
```

By default, Linux Docker commands may require `sudo`. You can add your user to the `docker` group to run them without `sudo`:

```bash
sudo usermod -aG docker "$USER"
```

Sign out and back in for the group change to take effect. **The `docker` group grants root-level privileges**; only add trusted users. See [Docker's post-installation steps](https://docs.docker.com/engine/install/linux-postinstall/) for details and alternatives.

## macOS

1. Check the [Docker Desktop for Mac requirements](https://docs.docker.com/desktop/setup/install/mac-install/) for your macOS version and processor (Apple silicon or Intel).
2. Download Docker Desktop from [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/).
3. Open the downloaded `.dmg` file and drag **Docker** to **Applications**.
4. Open Docker from Applications and follow the setup prompts. Wait until Docker Desktop reports that the engine is running.
5. In Terminal, verify the installation:

   ```bash
   docker run --rm hello-world
   ```

Alternatively, if you use Homebrew:

```bash
brew install --cask docker
```

After installing with Homebrew, open Docker from Applications to start it.

## Windows

Docker Desktop for Windows uses the WSL 2 backend for Linux containers. Check the [Windows requirements and installation guide](https://docs.docker.com/desktop/setup/install/windows-install/) before installing.

1. Install or update [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/windows/wsl/install). In an Administrator PowerShell window, run:

   ```powershell
   wsl --install
   ```

   Restart Windows if prompted. If WSL is already installed, update it with:

   ```powershell
   wsl --update
   ```

2. Download **Docker Desktop for Windows** from [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/), run the installer, and select the WSL 2 backend if prompted.
3. Start Docker Desktop and wait for it to report that Docker is running. If you use a WSL distribution, enable its integration in Docker Desktop under **Settings > Resources > WSL Integration**.
4. In PowerShell or a WSL terminal, verify the installation:

   ```powershell
   docker run --rm hello-world
   ```

## Verify Docker Compose

Docker Compose is installed as a Docker CLI plugin on the setups above. Confirm it is available with:

```bash
docker compose version
```
