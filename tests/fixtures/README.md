# Test fixtures

To regenerate test fixtures from the live API, use e.g. the following
command lines:

```sh
curl -fsLS -H 'Accept: application/xml' \
  'https://ovsyndication.kicker.de/API/universal/3.0/LeagueSeasonInfo/3/ligid/2/saison/2024_25' \
| XMLLINT_INDENT='    ' xmllint --format --pretty 1 - \
> tests/fixtures/league-season-info/league-2-2024_25.xml
```

```sh
curl -fsLS -H 'Accept: application/xml' \
  'https://ovsyndication.kicker.de/API/universal/3.0/LeagueSeasonInfo/3/ligid/6081/saison/2024_25' \
| XMLLINT_INDENT='    ' xmllint --format --pretty 1 - \
> tests/fixtures/league-season-info/league-6081-2024_25.xml
```
