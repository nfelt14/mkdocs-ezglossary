# Getting started

## Prerequisites

This plugin requires the
[material definition lists](https://squidfunk.github.io/mkdocs-material/reference/lists/)
to be active or any other plugin which generates
[html description lists](https://www.w3schools.com/HTML/html_lists.asp).

## Installation

    pip install mkdocs-ezglossary-plugin

## Usage

### Activation

Add the following lines to your `mkdocs.yml` plugins-section:

``` yaml
plugins:
  - search
  - ezglossary
```


### Defining glossary entries

Provided you use the material definition list, adding a glossary entry
just works by adding a definition list with section specifiers anywhere
in your documentation:

``` markdown
terms:glossary
:   A list of specialized words with their definitions
```

`terms` herby referes to the <terms:section> `terms` in which this glossary
entry will be added.

!!! Example

    Define the term `glossary` in the section `terms`:

    ``` markdown
    terms:glossary
    :   A list of specialized words with their definitions
    ```

    terms:glossary
    :   A list of specialized words with their definitions

### Linking to a glossary entry

Now link to this glossary definition using the following
syntax. This will produce a link to the definition in your documentation:

``` markdown
-   See the <section:term> for details
```

!!! Example

    Link to the previously defined `glossary` term in the `terms` section:

    ``` markdown
    -   See the <terms:glossary> for the definition of the term `glossary`
    ```

    -   See the <terms:glossary> for the definition of the term `glossary`

### Printing a summery

Now you can place a summary of all definitions anywhere in your
documentation:

``` markdown
# Terms and Definitions

<glossary::section>
```

!!! Example

    Lets generate the summary for the section `terms`:

    ``` markdown
    # Terms and Definitions

    <glossary::terms>
    ```

    This will produce the following summary. Note that the summary contains
    links to all definitions (`def`) and references (`ref`) to all terms
    in your documentation:

    <glossary::terms>
