<div align="center">

# Abalin Name Day <br> Home Assistant Integration

<img src="https://github.com/janfajessen/Abalin-Nameday---Home-Assistant/blob/353d58ea8d9ba5f4a876d1cff7fadd560ea1e653/brand/icon%402x.png" width="250"/>


![Version](https://img.shields.io/badge/version-2.1.0-blue?style=for-the-badge)
![HA](https://img.shields.io/badge/Home%20Assistant-2024.3+-orange?style=for-the-badge&logo=home-assistant)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python)
![HACS](https://img.shields.io/badge/HACS-Custom-41BDF5?style=for-the-badge&logo=homeassistantcommunitystore&logoColor=white)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Donate-yellow?style=for-the-badge&logo=buymeacoffee)](https://www.buymeacoffee.com/janfajessen)
[![Patreon](https://img.shields.io/badge/Patreon-Support-red?style=for-the-badge&logo=patreon)](https://www.patreon.com/janfajessen)
<!--[![Ko-Fi](https://img.shields.io/badge/Ko--Fi-Support-teal?style=for-the-badge&logo=ko-fi)](https://ko-fi.com/janfajessen)
[![GitHub Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-Support-pink?style=for-the-badge&logo=githubsponsors)](https://github.com/sponsors/janfajessen)
[![PayPal](https://img.shields.io/badge/PayPal-Donate-blue?style=for-the-badge&logo=paypal)](https://paypal.me/janfajessen)-->

</div>

A modern Home Assistant integration that brings daily name day sensors to your smart home — for 20 countries, fully configured through the UI, with no YAML required.

> Based on the original concept by [@viktak](https://github.com/viktak/ha-cc-abalin-nameday), rewritten from scratch for the current Abalin V2 API using modern Home Assistant architecture: config flow, `DataUpdateCoordinator`, `CoordinatorEntity`, and `DeviceInfo`.

---

## ✨ Why would you want this?

Name days are a wonderful tradition across much of Europe and beyond — a second birthday of sorts, celebrated in countries from Spain to Russia. But there are plenty of other reasons to track them too:

- 🎂 **Never miss wishing someone a happy name day** — family, friends, colleagues
- 🐶 **Naming a new pet?** Pick a date, find the name for that day — instant inspiration
- 👶 **Expecting a baby?** Browse names by their saint's day for a meaningful choice
- 👯 **Having twins?** Find two names that share the same day — or neighbouring ones
- 📅 **Planning events?** Tie a celebration to a name day for a personal touch
- 🤓 **Just curious** what your name day is in different countries

---

## 🌍 Supported countries

| <sub>Country</sub> | <sub>Code</sub> | <sub>Country</sub> | <sub>Code</sub> |
|---|---|---|---|
| <sub>🇦🇹 Österreich</sub> | <sub>`at`</sub> | <sub>🇱🇹 Lietuva</sub> | <sub>`lt`</sub> |
| <sub>🇧🇬 България</sub> | <sub>`bg`</sub> | <sub>🇵🇱 Polska</sub> | <sub>`pl`</sub> |
| <sub>🇭🇷 Hrvatska</sub> | <sub>`hr`</sub> |  <sub>🇸🇰 Slovensko</sub> | <sub>`sk`</sub> |
| <sub>🇨🇿 Česká republika</sub> | <sub>`cz`</sub> | <sub>🇪🇸 España/Espanya/Espainia</sub> | <sub>`es`</sub> |
| <sub>🇩🇰 Danmark</sub> | <sub>`dk`</sub> | <sub>🇸🇪 Sverige</sub> | <sub>`se`</sub> |
| <sub>🇪🇪 Eesti</sub> | <sub>`ee`</sub> |<sub>🇩🇪 Deutschland</sub> | <sub>`de`</sub> |
| <sub>🇫🇮 Suomi / Finland</sub> | <sub>`fi`</sub> | <sub>🇺🇸 United States</sub> | <sub>`us`</sub> |
| <sub>🇫🇷 France</sub> | <sub>`fr`</sub> |  <sub>🇭🇺 Magyarország</sub> | <sub>`hu`</sub> |
| <sub>🇬🇷 Ελλάδα</sub> | <sub>`gr`</sub> | <sub>🇱🇻 Latvija</sub> | <sub>`lv`</sub> |
| <sub>🇮🇹 Italia</sub> | <sub>`it`</sub> |
---


---

## ⚙️ Features

- 🖱️ **Full UI setup** — add from Settings → Integrations, no `configuration.yaml` needed
- 📅 **Two sensors per country** — today's and tomorrow's name day
- 🔄 **One API call per day** — efficient and respectful of the free API
- 🏠 **Device page** — sensors grouped together, with linked automations and scripts visible
- 🌐 **Translated UI** — English, Spanish and Catalan included
- ⏰ **Timezone auto-detected** from your HA configuration
- ➕ **Multi-country** — add the integration multiple times, one per country

---

## 📦 Installation

### Via HACS (recommended)

1. Open HACS → Integrations → ⋮ → **Custom repositories**
2. Add this repository URL, category: **Integration**
3. Install **Abalin Name Day**
4. Restart Home Assistant

<img src="https://github.com/janfajessen/Abalin-Nameday---Home-Assistant/blob/353d58ea8d9ba5f4a876d1cff7fadd560ea1e653/brand/icon%402x.png" width="100"/>

### Manual

1. Copy the `abalin_nameday` folder into `config/custom_components/`
2. Restart Home Assistant

---

## 🔧 Configuration

1. Go to **Settings → Devices & Integrations → Add Integration**
2. Search for **Name Day** or **Abalin**
3. Select a country from the dropdown
4. Done — sensors appear immediately, no restart needed

Repeat to add multiple countries simultaneously.

---

## 📡 Entities

For each configured country, two sensors are created and grouped under a single device:

| <sub>Entity</sub> | <sub>Example ID</sub> | <sub>Description</sub> | <sub>Icon</sub> |
|---|---|---|---|
| <sub>Today's name day</sub> | <sub>`sensor.nameday_spain_today`</sub> | <sub>Names celebrated today</sub> | <sub>`mdi:account-star`</sub> |
| <sub>Tomorrow's name day</sub> | <sub>`sensor.nameday_spain_tomorrow`</sub> | <sub>Names celebrated tomorrow</sub> | <sub>`mdi:account-clock`</sub> |



Each sensor also exposes `country` and `timezone` as state attributes.

---

## 🤖 Automation examples

### Morning name day greeting notification

```yaml
automation:
  - alias: "Name day morning greeting"
    trigger:
      - platform: time
        at: "08:00:00"
    condition:
      - condition: template
        value_template: "{{ states('sensor.nameday_spain_today') not in ['', 'unavailable', 'unknown'] }}"
    action:
      - action: notify.mobile_app
        data:
          title: "🎉 Name Day Today!"
          message: >
            Today's name day: {{ states('sensor.nameday_spain_today') }}
            Tomorrow: {{ states('sensor.nameday_spain_tomorrow') }}
```

### Announce on smart speaker

```yaml
automation:
  - alias: "Name day speaker announcement"
    trigger:
      - platform: time
        at: "09:00:00"
    action:
      - action: tts.speak
        data:
          media_player_entity_id: media_player.living_room
          message: >
            Good morning! Today's name day is for
            {{ states('sensor.nameday_spain_today') }}.
```

### Persistent notification on the dashboard

```yaml
automation:
  - alias: "Name day dashboard card"
    trigger:
      - platform: time
        at: "00:01:00"
    action:
      - action: persistent_notification.create
        data:
          title: "🗓️ Name Day"
          message: >
            **Today:** {{ states('sensor.nameday_spain_today') }}
            **Tomorrow:** {{ states('sensor.nameday_spain_tomorrow') }}
          notification_id: nameday_daily
```

### Multi-country morning briefing

```yaml
automation:
  - alias: "Multi-country name day briefing"
    trigger:
      - platform: time
        at: "07:30:00"
    action:
      - action: notify.mobile_app
        data:
          title: "🌍 Name Days Today"
          message: >
            🇪🇸 Spain: {{ states('sensor.nameday_spain_today') }}
            🇫🇷 France: {{ states('sensor.nameday_france_today') }}
            🇩🇪 Germany: {{ states('sensor.nameday_germany_today') }}
```

### Lovelace card (markdown)

```yaml
type: markdown
title: 🗓️ Name Days
content: >
  | | Today | Tomorrow |
  |--|--|--|
  | 🇪🇸 | {{ states('sensor.nameday_spain_today') }} | {{ states('sensor.nameday_spain_tomorrow') }} |
  | 🇫🇷 | {{ states('sensor.nameday_france_today') }} | {{ states('sensor.nameday_france_tomorrow') }} |
```
## 🔍 Service: query any date

Beyond the daily sensors, this integration provides a service that lets you query name days for **any date of the year** — useful for finding the perfect name for a pet, a baby, or just satisfying your curiosity.

### `abalin_nameday.get_nameday_for_date`

| Field | Required | Description |
|-------|----------|-------------|
| `day` | ✅ | Day of the month (1–31) |
| `month` | ✅ | Month number (1–12) |
| `country` | ☑️ optional | Country code (e.g. `es`). Omit to get all 19 countries at once. |

The service returns data directly — find it under **Developer Tools → Services** in your HA interface.

**Single country response** (e.g. Spain, July 25th):
```json
{
  "day": 25,
  "month": 7,
  "country": "es",
  "country_name": "Spain",
  "names": "Santiago, Jaime"
}
```

**All countries response** (no country specified):
```json
{
  "day": 25,
  "month": 7,
  "namedays": {
    "es": "Santiago, Jaime",
    "fr": "Jacques",
    "de": "Jakob",
    "it": "Giacomo",
    "pl": "Jakub"
  }
}
```

### Use in automations

```yaml
action:
  - action: abalin_nameday.get_nameday_for_date
    data:
      day: 25
      month: 7
      country: es
    response_variable: result
  - action: notify.mobile_app
    data:
      message: "Names for July 25th in Spain: {{ result.names }}"
```

---

## 🌐 API

This integration uses the [Abalin Name Day API V2](https://nameday.abalin.net) — a free, open-source project. Data is fetched once per day to keep load minimal.

---

## 🌱 Contributing

Pull requests are welcome!

---

*If this integration is useful to you, consider giving it a ⭐ on GitHub.*
Or consider supporting development!

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Donate-yellow?style=for-the-badge&logo=buymeacoffee)
](https://www.buymeacoffee.com/janfajessen) 
[![Patreon](https://img.shields.io/badge/Patreon-Support-red?style=for-the-badge&logo=patreon)](https://www.patreon.com/janfajessen)
</div>


## 📄 License

[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)

---

## 🙏 Credits

- Original integration concept: [@viktak](https://github.com/viktak/ha-cc-abalin-nameday)
- Name Day API: [nameday.abalin.net](https://nameday.abalin.net) by [@xnekv03](https://github.com/xnekv03)
