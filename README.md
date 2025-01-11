# Информационная панель


> Уведомляет о новых письмах в ТГ. Возможность подключения нескольких почтовых
> ящиков.
### Gitlab: https://gitlab.port-tranzit.ru/pt-sandbox/baracode_informer_PT.git

### Github: https://github.com/Ruslanch0s/baracode_informer_PT.git

- Информационная панель для водителей установленная на Новороссийском авто
  терминале (Владимировка) в Пентагоне.
- Нужна для сканирования штрихкода с ТТН и определения статуса авто (куда ехать
  или ждать)

# Телеграм бот для Mail.ru почты



## Table of Contents

* [Антифлуд](#)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)

<!-- * [License](#license) -->

## Антифлуд

###Отдельно для хендлера

1) utils.antiflood import rate_limit
2) @rate_limit(`seconds`, `command`)
    - `seconds` is required
      ###Для всех хендлеров
1) middlewares/antiflood... > 2 (2 is seconds)

## Занятые порты на MacOC

sudo lsof -i :5432
kill <pid>

## Handlers

https://core.telegram.org/bots/api

- Register Handler - Getting updates (Update object)
- Get message - Available types for 1 step
- Send message - Available methods

## Screenshots

<!-- If you have screenshots you'd like to share, include them here. -->

## Setup

What are the project requirements/dependencies? Where are they listed? A
requirements.txt or a Pipfile.lock file perhaps? Where is it located?

Proceed to describe how to install / setup one's local environment / get
started with the project.

## Usage

How does one go about using it?
Provide various use cases and code examples here.

`write-your-code-here`

## Project Status

Project is: _in progress_ / _complete_ / _no longer being worked on_. If you
are no longer working on it, provide reasons why.

## Room for Improvement

Include areas you believe need improvement / could be improved. Also add TODOs
for future development.

Room for improvement:

- Improvement to be done 1
- Improvement to be done 2

To do:

- Feature to be added 1
- Feature to be added 2

## Acknowledgements

Give credit here.

- This project was inspired by...
- This project was based on [this tutorial](https://www.example.com).
- Many thanks to...

## Contact

Created by [@flynerdpl](https://www.flynerd.pl/) - feel free to contact me!


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
