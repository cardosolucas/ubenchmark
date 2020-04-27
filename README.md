# Ubenchmark
Ubenchmark is a framework for benchmarking machine learning models. With him, you can measure the hardware consumption of each step of the traditional pipeline and add your own steps.

In addition, the framework allows the simulation of an REST API for predictions, simulating a server in production.

You can use this REST API to perform stress tests using tools like Apache JMeter.

## Usage

 - Install cookiecutter:
 `pip install cookiecutter`
 - Get the template of the project:
 `cookiecutter https://github.com/cardosolucas/ubenchmark.git`
 - Write your code (a example can be found [here](https://github.com/cardosolucas/houseprices-example))
 - Use the Makefile to test and run the project:
 `make tests && make dryrun`
 - You can also build a Docker image and run the container:
 `make docker-build && make docker-run`
 - You can run the container and get the metrics with [cAdvisor](https://github.com/google/cadvisor).

## Warning
Do **NOT** use this in production. This framework is for development tests only. 