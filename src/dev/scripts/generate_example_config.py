from flemmarr.clients.sonarr_client.models import IndexerResource, Field
import yaml
from pathlib import Path

example = IndexerResource(
    name="MyIndexer",
    implementation="Torznab",
    config_contract="torznabSettings",
    enable_rss=True,
    enable_automatic_search=True,
    fields=[
        Field(name="url", value="https://example.com"),
        Field(name="apiKey", value="myapikey"),
    ]
)

yaml_data = {"indexer": [example.to_dict()]}

output_path = Path("config/example_config.yml")
output_path.parent.mkdir(exist_ok=True, parents=True)
output_path.write_text(yaml.dump(yaml_data, sort_keys=False))

print(f"✅ Example YAML config written to {output_path}")