"""Tests of configuration and login."""

import tiledb_cloud
import tiledb_cloud.config


def test_login_bare_host(monkeypatch, tmp_path):
    """Accept a bare host, store it with https scheme."""
    monkeypatch.setattr(
        tiledb_cloud.client.config,
        "default_config_file",
        tmp_path.joinpath("cloud.json"),
    )
    monkeypatch.setattr(
        tiledb_cloud.client.config,
        "config",
        tiledb_cloud.config.configuration.Configuration(),
    )
    monkeypatch.setattr(tiledb_cloud.client.config, "logged_in", False)
    monkeypatch.setattr(tiledb_cloud.client, "client", tiledb_cloud.client.Client())
    tiledb_cloud.login(token="foo", host="bar")
    assert tiledb_cloud.config.config.host == "https://bar"


def test_login_bare_host_bis():
    """Check on the first."""
    assert tiledb_cloud.config.config.host != "https://bar"
