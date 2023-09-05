<img src="./microcks-banner.png" width="600"> 

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/microcks/microcks/build-verify.yml?logo=github&style=for-the-badge)](https://github.com/microcks/microcks/actions)
[![Container](https://img.shields.io/badge/dynamic/json?color=blueviolet&logo=docker&style=for-the-badge&label=Quay.io&query=tags[0].name&url=https://quay.io/api/v1/repository/microcks/microcks/tag/?limit=10&page=1&onlyActiveTags=true)](https://quay.io/repository/microcks/microcks?tab=tags)
[![Version](https://img.shields.io/maven-central/v/io.github.microcks/microcks?color=blue&style=for-the-badge)]((https://search.maven.org/artifact/io.github.microcks/microcks))
[![License](https://img.shields.io/github/license/microcks/microcks?style=for-the-badge&logo=apache)](https://www.apache.org/licenses/LICENSE-2.0)
[![Project Chat](https://img.shields.io/badge/chat-on_zulip-pink.svg?color=ff69b4&style=for-the-badge&logo=zulip)](https://microcksio.zulipchat.com/)


# Microcks - Kubernetes native tool for API Mocking & Testing

Microcks is a platform for turning your API and microservices assets - *OpenAPI specs*, *AsyncAPI specs*, *gRPC protobuf*, *GraphQL schema*, *Postman collections*, *SoapUI projects* - into live mocks in seconds.

It also reuses these assets for running compliance and non-regression tests against your API implementation. We provide integrations with *Jenkins*, *GitHub Actions*, *Tekton* and many others through a simple CLI.

## Getting Started

* [Documentation](https://microcks.io/documentation/getting-started/)

To get involved with our community, please make sure you are familiar with the project's [Code of Conduct](./CODE_OF_CONDUCT.md).

## Build Status

The current development version is `1.8.0-SNAPSHOT`. [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/microcks/microcks/build-verify.yml?branch=1.8.x&logo=github&style=for-the-badge)](https://github.com/microcks/microcks/actions)

## Versions

Here are the naming conventions we're using for current releases, ongoing development maintenance activities.

| Status      | Version          | Branch   | Container images tags |
| ----------- |------------------| -------- |-----------------------|
| Stable      | `1.7.1`          | `master` | `1.7.1`, `latest`     |
| Dev         | `1.8.0-SNAPSHOT` | `1.8.x`  | `nightly`             |
| Maintenance | `1.7.2-SNAPSHOT` | `1.7.x`  | `maintenance`         |


## How to build Microcks

The build instructions are available in the [contribution guide](CONTRIBUTING.md).

## Thanks to community!

[![Stargazers repo roster for @microcks/microcks](https://reporoster.com/stars/microcks/microcks)](https://github.com/microcks/microcks/stargazers)
[![Forkers repo roster for @microcks/microcks](https://reporoster.com/forks/microcks/microcks)](https://github.com/microcks/microcks/network/members)
