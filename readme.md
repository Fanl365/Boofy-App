<p align="center"><img src="./assets/boofy-banner.png" width="100%" alt="Boofy — Build · Connect · Grow" /></p>

# Boofy App

Boofy App is the frontend workspace for the Boofy DeFi project. This repository contains the user-facing application, wallet interactions, vault views, configuration, and supporting UI components.

> **Development status:** active rebrand and engineering migration. Production domains, token symbols, contract addresses, and deployment identifiers are considered unverified until explicitly published by the Boofy team.

## Project goals

- Provide a clean multichain DeFi user experience.
- Integrate Boofy vault and strategy data from the Boofy API.
- Keep wallet and chain interactions transparent and auditable.
- Maintain a reusable frontend architecture for future Boofy products.

## Development

```bash
yarn
yarn validate
yarn start
```

The local development server runs at `http://localhost:3000/` unless configured otherwise.

## Current work

The project is moving through four active tracks:

1. Boofy visual identity and application branding.
2. Configuration cleanup and replacement of upstream deployment identifiers.
3. API integration and multichain data validation.
4. Test, build, and release hardening.

See [ROADMAP.md](ROADMAP.md) and the repository Issues for current engineering work.

## Repository history

Boofy App preserves the upstream development history used as the technical foundation of this project. Historical commits retain their original authorship and dates; current Boofy development is tracked separately through new commits and issues.

## Team

- **Fan Long** — Co-Founder
- **David Woo** — Developer
- **Tyler Casselman** — Developer
- **Albert Jones** — Developer

See [BOOFY_TEAM.md](BOOFY_TEAM.md).

## Contributing

Contributions and technical reviews are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Migration notice

Before using this code in production, read [BOOFY_MIGRATION_NOTICE.md](BOOFY_MIGRATION_NOTICE.md). Upstream addresses, transaction hashes, token identifiers, domains, and social references are not automatically valid Boofy production values.

## License

See [LICENSE](LICENSE).
