<div align="center">

# 🗓️ Abalin Name Day <br> Home Assistant Integration

<img src="brands/icon@2x.png" width="450"/>


![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge)
![HA](https://img.shields.io/badge/Home%20Assistant-2024.3+-orange?style=for-the-badge&logo=home-assistant)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python)
![HACS](https://img.shields.io/badge/HACS-Custom-41bdf5?style=for-the-badge)
[![Ko-Fi](https://img.shields.io/badge/Ko--Fi-Support-teal?style=for-the-badge&logo=ko-fi)](https://ko-fi.com/janfajessen)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Donate-yellow?style=for-the-badge&logo=buymeacoffee)](https://www.buymeacoffee.com/janfajessen)
[![Patreon](https://img.shields.io/badge/Patreon-Support-red?style=for-the-badge&logo=patreon)](https://www.patreon.com/janfajessen)
[![GitHub Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-Support-pink?style=for-the-badge&logo=githubsponsors)](https://github.com/sponsors/janfajessen)
<!--[![PayPal](https://img.shields.io/badge/PayPal-Donate-blue?style=for-the-badge&logo=paypal)](https://paypal.me/janfajessen)-->

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

<sub>

| Flag | Country | Code | Flag | Country | Code |
|------|---------|------|------|---------|------|
| 🇦🇹 | Austria | `at` | 🇱🇹 | Lithuania | `lt` |
| 🇧🇬 | Bulgaria | `bg` | 🇵🇱 | Poland | `pl` |
| 🇭🇷 | Croatia | `hr` | 🇷🇺 | Russia | `ru` |
| 🇨🇿 | Czech Republic | `cz` | 🇸🇰 | Slovakia | `sk` |
| 🇩🇰 | Denmark | `dk` | 🇪🇸 | Spain | `es` |
| 🇪🇪 | Estonia | `ee` | 🇸🇪 | Sweden | `se` |
| 🇫🇮 | Finland | `fi` | 🇺🇸 | United States | `us` |
| 🇫🇷 | France | `fr` | 🇩🇪 | Germany | `de` |
| 🇬🇷 | Greece | `gr` | 🇭🇺 | Hungary | `hu` |
| 🇮🇹 | Italy | `it` | 🇱🇻 | Latvia | `lv` |

</sub>

---

## 📸 Screenshot

![Sensor screenshot](https://raw.githubusercontent.com/viktak/ha-cc-abalin-nameday/main/images/abalin-nameday-sample-screenshot.png)

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

<sub>

| Entity | Example ID | Description | Icon |
|--------|-----------|-------------|------|
| Today's name day | `sensor.nameday_spain_today` | Names celebrated today | `mdi:account-star` |
| Tomorrow's name day | `sensor.nameday_spain_tomorrow` | Names celebrated tomorrow | `mdi:account-clock` |

</sub>

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
      - service: notify.mobile_app
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
      - service: tts.speak
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
      - service: persistent_notification.create
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
      - service: notify.mobile_app
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

---

## 🌐 API

This integration uses the [Abalin Name Day API V2](https://nameday.abalin.net) — a free, open-source project. Data is fetched once per day to keep load minimal.

---

## 🌱 Contributing

Pull requests are welcome! To add a new translation, copy `translations/en.json`, translate the strings, and submit a PR.

---

## 📄 License

[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)

---

## 🙏 Credits

- Original integration concept: [@viktak](https://github.com/viktak/ha-cc-abalin-nameday)
- Name Day API: [nameday.abalin.net](https://nameday.abalin.net) by [@xnekv03](https://github.com/xnekv03)
