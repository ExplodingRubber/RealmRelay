# RealmRelay

**A unified game server management platform for dedicated servers.**

RealmRelay is a host management platform designed to simplify the monitoring and management of dedicated game servers across multiple machines and environments.

The long-term goal of RealmRelay is to provide a single management solution for users who operate multiple servers, multiple games, or multiple physical and virtual hosts.

Instead of maintaining separate scripts and tools for each game, RealmRelay is being built around a modular agent architecture that can discover, monitor, configure, and manage dedicated game servers through a consistent interface.

---

# Project Status

**Current Version:** 0.0.52  
**Development Stage:** Foundation / Agent Development

RealmRelay is currently under active development.

The current focus is building the core agent architecture, configuration framework, host monitoring capabilities, and API foundation that future game server integrations will use.

At this stage, RealmRelay is not intended for production use.

---

# Current Features

## RealmRelay Agent

The RealmRelay Agent is the foundation of the platform.

Current capabilities:

- Runs as a standalone Python application
- Provides a FastAPI-based API
- Identifies the host machine
- Reports system information
- Tracks host uptime
- Provides agent status information

Current status endpoint provides:

- Agent name
- Agent version
- Hostname
- Device uptime
- Online status

---

## Host Information

RealmRelay can currently report host details including:

- Hostname
- Operating system
- OS version
- CPU information
- Logical processor count
- Memory allocation
- System architecture

---

## System Monitoring

RealmRelay currently provides basic system metrics:

- CPU utilization
- Memory usage
- Disk usage
- Available resources

These metrics will become the foundation for future server health monitoring.

---

## Configuration Management

RealmRelay uses a centralized configuration system.

Current configuration features:

- User-editable configuration file
- Configurable API port
- Configurable agent name
- Configurable version number
- Automatic creation of default configuration

Example:

```json
{
    "agent_name": "RealmRelay Agent",
    "version": "0.0.52",
    "api_host": "0.0.0.0",
    "api_port": 42069
}
