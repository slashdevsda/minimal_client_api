from algolia_minimal.health import HealthClient


h = HealthClient.create('', '')
print(h.status())
print(h.status("c10-eu", "c4-eu"))
print(h.incidents())
print(h.incidents("c10-eu", "c4-eu"))
