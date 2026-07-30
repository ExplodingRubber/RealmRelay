# RealmRelay

**A unified game server management platform for dedicated servers.**

RealmRelay is a platform designed to simplify the management of dedicated game servers across multiple machines and environments.

The goal of RealmRelay is to provide a single management solution for game server owners who run multiple servers, multiple games, or multiple physical and virtual hosts.

Instead of maintaining individual scripts for each game, RealmRelay provides a modular system that can discover, monitor, configure, and manage dedicated game servers through a consistent interface.

---

# Project Status

**Current Version:** 0.0.2  
**Development Stage:** Foundation / Early Development

RealmRelay is currently under active development. The current focus is building the core agent architecture, configuration system, and host management framework that future game integrations will use.

At this stage, RealmRelay is not yet intended for production use.

---

# Current Features

## RealmRelay Agent

The RealmRelay Agent is the foundation of the platform.

Current capabilities:

- Starts as a standalone Python application
- Identifies the host machine it is running on
- Reports:
  - Hostname
  - Operating system
  - OS version
  - CPU information
  - Logical processor count
  - Memory allocation

---

## Configuration Management

RealmRelay includes a centralized configuration system designed to avoid hardcoded paths and machine-specific assumptions.

The configuration system will eventually manage:

- Installed games
- Server locations
- Host settings
- Discovery preferences
- Agent settings

---

## Path Management

RealmRelay uses an abstraction layer for application and data locations.

This allows future installations to support different environments, including:

- Development environments
- Windows installations
- Linux installations
- Containerized deployments

---

# Project Goals

RealmRelay is being designed around several core principles.

## No Hardcoded Server Paths

Game servers can exist anywhere.

RealmRelay should discover and manage servers without requiring users to modify scripts every time a server location changes.

---

## Modular Game Support

Each game server should have its own management module.

Examples:

- Palworld
- Minecraft
- ARK: Survival Evolved
- Other SteamCMD-based servers
- Future dedicated server platforms

Each module will define:

- How a server is detected
- How it is installed
- How it is updated
- How it is monitored
- How it is managed

---

## Host-Based Architecture

RealmRelay is designed around a host and agent model.

A machine running RealmRelay Agent can:

- Report hardware information
- Identify installed servers
- Monitor server status
- Execute approved management actions

A central console can then manage multiple hosts.

---

# Planned Features

## First-Run Setup

RealmRelay will guide users through initial configuration.

Example workflow:

1. Install RealmRelay Agent
2. Identify the host system
3. Ask whether game servers already exist
4. Scan approved locations
5. Detect installed servers
6. Offer installation options for missing services

---

## Game Server Discovery

RealmRelay will be able to identify installed servers by using game-specific detection modules.

Discovery may include:

- Known server executables
- Configuration files
- Directory structures
- Installed service information

Users will control what locations RealmRelay scans.

---

## Game Server Installation

RealmRelay will eventually provide guided installation workflows.

Examples:

- Install SteamCMD
- Create server directories
- Download server files
- Configure initial settings
- Register servers for management

---

## Host Management

Future versions will include host-level management:

- CPU usage
- Memory usage
- Storage information
- Uptime
- Operating system information
- Service status
- Restart/shutdown controls

---

## Management Console

The long-term goal is a dedicated management application that allows users to:

- View all hosts
- View all game servers
- Manage configurations
- Start, stop, and restart servers
- Monitor activity

---

# Architecture

Current structure:

```text
RealmRelay
│
├── agent
│   ├── main.py
│   └── host.py
│
├── core
│   └── paths.py
│
├── config
│   └── config_manager.py
│
├── games
│
├── models
│
├── utils
│
├── tests
│
└── data
```

The project is intentionally separated into modules to keep development maintainable and allow future contributors to understand the codebase.

---

# Supported Platforms

RealmRelay is being designed with cross-platform support in mind.

Target platforms:

- Windows
- Linux

The goal is for the same agent architecture to support different server environments regardless of operating system.

---

# Security and Privacy

RealmRelay is designed to be transparent.

The software will only perform management actions on systems where it has been intentionally installed and configured.

Users should understand that RealmRelay may:

- Scan configured locations for game server files
- Monitor server configuration changes
- Collect system information required for management features

No hidden scanning or remote management should occur without user configuration.

---

# Development

RealmRelay is currently written in Python.

Development environment:

- Python 3.x
- FastAPI
- Uvicorn
- Pydantic
- psutil

Additional dependencies will be added as features are implemented.

---

# Contributing

RealmRelay is currently in early development.

As the project matures, contribution guidelines, issue templates, and development documentation will be added.

---

# License

License information will be added before the first public release.

---

# Disclaimer

RealmRelay is designed for users managing their own dedicated server environments.

Users are responsible for ensuring they have permission to install, monitor, and manage any systems, software, or game servers controlled by RealmRelay.
