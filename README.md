# RealmControl

RealmControl is an open-source, cross-platform game server management platform.

## Status

Early Development (0.0.1)

## Goals

- Cross-platform support (Windows/Linux)
- Agent-based architecture
- Multi-host management
- Game server discovery
- Automated deployment
- SteamCMD integration
- Discord integration

## Architecture

RealmControl consists of:

### RealmControl Agent

Installed on managed hosts.

Responsibilities:
- Identify host hardware and operating system
- Monitor managed game servers
- Perform approved management actions

### RealmControl Console

User-facing management application.

Responsibilities:
- Manage hosts
- Manage games
- View status and logs

### RealmControl Core

Shared business logic.

Responsibilities:
- Game management
- Discovery
- Updates
- Backups