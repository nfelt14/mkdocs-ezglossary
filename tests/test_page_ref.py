import mock

from yaxp import xpath as xp

mycommand = mock.Page(
    title="My Command",
    file="mycommand.md",
    ctype="markdown",
    content="""
---
ezglossary:
  - cmd4
  - "cmd5#world2"
  - page: cmd2
  - page: "cmd3#world"
  - page:
    - help1
    - term2: hello
    - term3: details
  - cmd:
    - help2
    - help3: help
---
# Help page

## Overview

## Help

## Details
""")

commands = mock.Page(
    title="Commands",
    file="commands.md",
    content="""
<body>
    <glossary::page>

    <glossary::cmd>

    <glossary::_>
</body>


""")


def test_page_ref_simple(config):
    pages = mock.render([mycommand, commands], config)

    dd = xp.dd().ul().li().a(href="../mycommand.md#",
                             text="My Command")
    dl = xp.dl(_class="mkdocs-ezglossary-summary", _id="page")
    dl = dl.has(xp.dt(text="help1"))
    dl = dl.has(dd)
    assert len(pages['commands.md'].xpath(str(dl))) == 1

    dd = xp.dd().ul().li().a(href="../mycommand.md#",
                             text="My Command")
    dl = xp.dl(_class="mkdocs-ezglossary-summary", _id="cmd")
    dl = dl.has(dd)
    dl = dl.has(xp.dt(text="help2"))
    assert len(pages['commands.md'].xpath(str(dl))) == 1


def test_page_ref_anchor(config):
    pages = mock.render([mycommand, commands], config)

    dd = xp.dd().ul().li().a(href="../mycommand.md#hello",
                             text="My Command")
    dl = xp.dl(_class="mkdocs-ezglossary-summary", _id="page")
    dl = dl.has(xp.dt(text="term2"))
    dl = dl.has(dd)
    assert len(pages['commands.md'].xpath(str(dl))) == 1


def test_page_ref_direct(config):
    pages = mock.render([mycommand, commands], config)

    dd = xp.dd().ul().li().a(href="../mycommand.md#",
                             text="My Command")
    dl = xp.dl(_class="mkdocs-ezglossary-summary", _id="page")
    dl = dl.has(xp.dt(text="cmd2"))
    dl = dl.has(dd)
    assert len(pages['commands.md'].xpath(str(dl))) == 1


def test_page_ref_direct_anchor(config):
    pages = mock.render([mycommand, commands], config)

    dd = xp.dd().ul().li().a(href="../mycommand.md#world",
                             text="My Command")
    dl = xp.dl(_class="mkdocs-ezglossary-summary", _id="page")
    dl = dl.has(xp.dt(text="cmd3"))
    dl = dl.has(dd)
    assert len(pages['commands.md'].xpath(str(dl))) == 1


def test_page_ref_default_section(config):
    pages = mock.render([mycommand, commands], config)

    dd = xp.dd().ul().li().a(href="../mycommand.md#",
                             text="My Command")
    dl = xp.dl(_class="mkdocs-ezglossary-summary", _id="_")
    dl = dl.has(xp.dt(text="cmd4"))
    dl = dl.has(dd)
    assert len(pages['commands.md'].xpath(str(dl))) == 1


def test_page_ref_default_section_anchor(config):
    pages = mock.render([mycommand, commands], config)

    dd = xp.dd().ul().li().a(href="../mycommand.md#world2",
                             text="My Command")
    dl = xp.dl(_class="mkdocs-ezglossary-summary", _id="_")
    dl = dl.has(xp.dt(text="cmd5"))
    dl = dl.has(dd)
    assert len(pages['commands.md'].xpath(str(dl))) == 1
