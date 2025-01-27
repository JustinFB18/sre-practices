# sre-practices
A repository showcasing Site Reliability Engineering (SRE) practices, including automation, monitoring and others.


## Table of Contents

- [Introduction](#introduction)
- [SRE Practices](#sre-practices)
  - [Automation](#automation)
  - [Monitoring](#monitoring)
- [Repository Contents](#repository-contents)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [License](#license)


## Introduction

Site Reliability Engineering (SRE) is a discipline that incorporates aspects of software engineering and applies them to infrastructure and operations problems. The main goals are to create scalable and highly reliable software systems. SRE practices are based on the principles of automation, monitoring, incident management, postmortems, capacity planning, change management, security, disaster recovery, documentation, on-call, training, and culture.

This repository showcases SRE practices, including automation, monitoring, incident management, postmortems, capacity planning, change management, security, disaster recovery, documentation, on-call, training, and culture.

\[[Back to Top](#table-of-contents)\]

## SRE Practices

### Automation

Automation is a key aspect of SRE practices. It involves using tools and scripts to perform repetitive tasks, such as provisioning infrastructure, deploying applications, and monitoring systems. Automation helps reduce human error, increase efficiency, and improve reliability.

#### Tools

- [Terraform](https://www.terraform.io/): Infrastructure as Code (IaC) tool that allows you to define and provision infrastructure using declarative configuration files.
- [Ansible](https://www.ansible.com/): Configuration management tool that allows you to automate the provisioning and configuration of servers.
- [Jenkins](https://www.jenkins.io/): Automation server that allows you to automate tasks such as building, testing, and deploying software.
- [Prometheus](https://prometheus.io/): Monitoring and alerting toolkit that allows you to collect and store metrics from your systems.
- [Grafana](https://grafana.com/): Visualization tool that allows you to create dashboards and graphs from your metrics data.

### Monitoring

Section on progress...

## Repository Contents

This repository contains the following directories:

- monitoring: Contains scripts of Python for monitoring a website.
    - website_monitoring.py: A Python script that checks the status of a website and sends an email notification if the website is down.
- .github/workflows: Contains GitHub Actions workflows.
    - ci.yml: A GitHub Actions workflow that runs on every push to the repository. It runs the website_monitoring.py script to check the status of a website.

## Getting Started

To get started with this repository, you can clone it to your local machine using the following command:

```bash
git clone https://github.com/JustinFB18/sre-practices.git
```

You can then explore the contents of the repository and start using the scripts and workflows provided.

### How to Contribute

Guidelines on how to contribute to this repository are available in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

### License

This repository is licensed under the MIT License. See `LICENSE` for more information.
