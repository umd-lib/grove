# Test Plan

## Introduction

This document provides a basic test plan that verifies as much application
functionality as feasible.

The intention is to provide basic assurance that the application is functional,
and guard against regressions.

**This document is not intended to be an exhaustive test plan.**

## Test Plan Assumptions

This test plan assumes that the user can log in via CAS as an administrator
(i.e., is a member of the "Grove-Administrator" group in Grouper).

The test plan steps are specified using URLs for the Kubernetes "test"
namespace, as that seems to be the most useful. Unless otherwise specified,
test steps should also work in the local development environment.

## Grove Test Plan

### 1) Grove Home Page

1.1) In a web browser, go to

<https://grove-test.lib.umd.edu/>

The Grove home page will be displayed.

1.2) On the Grove home page, verify that:

* The UMD favicon is displayed in the browser tab
* The appropriate SSDR environment banner is displayed
* The page contains a "Log In" button

**Note:** In the local development environment, the UMD favicon will *not* be
displayed.

1.3) At the bottom of the page, verify that the footer:

* Displays the application version number
* Has a "Web Accessibility" link

1.3.1) Left-click the "Web Accessibility" link. Verify that the web
accessibility page on the university website is displayed.

1.3.2) Go back to the Grove home page.

1.4) Left-click the "Log In" button. After logging in via CAS, verify that the
"Vocabularies" page is displayed.

### 2) Vocabulary Import

2.1) On the "Vocabularies" page, left-click the "Import" link in the navigation
bar. Verify that the "Import Vocabulary" page is displayed.

2.2) Download the
     [grove-test-collection.jsonld](resources/grove-test-collection.jsonld)
     file to the local workstation.

2.3) On the "Import Vocabulary" page, fill out the following fields:

| Field | Value |
| ----- | ----- |
| URI | `http://example.com/grove-test#` |
| File | <Select the downloaded "grove-test-collection.jsonld" file> |
| RDF Format | `JSON-LD` |

and left-click the "Import" button. Verify that a "Vocabulary: Grove-Test"
page is displayed, with a notification that the import was successful.

### 3) Vocabulary Page

3.1) On the "Vocabulary: Grove-Test" page, verify that:

* There is a "Details" section

* A "Terms" section with two terms displayed:
  * `0001-TEST`
  * `0002-TEST`

* A "Create New Term" section

3.2) Expand the "Details" section by left-clicking on the "Details" header.
The section will expand to display a form with the following fields:

* URI - populated with `http://example.com/grove-test#`
* Label - populated with `Grove-Test`
* Description - \<Blank>
* Preferred prefix  - \<Blank>

3.3) In the "Preferred prefix" field, enter `test` and left-click the "Update"
button. Verify that the page refreshes with a notification that the vocabulary
was updated. Expand the "Details" section and verify that the "Preferred prefix"
field contains `test`.

3.4) In the "Create New Term" section:

* Enter `0003-TEST` in the "Name" field
* Left-click the drop-down and select `Class`

then left-click the "Add Term" button. Verify that the "Terms" section
is updated to include a `0003-TEST` entry with `rdf:type: rdfs:Class`,
and that the form in the "Create New Term" section shows an empty "Name" field.

3.5) Left-click the "Publish" button at the top of the page. Verify that a
"Status" field of "Published" is displayed, along with an "Unpublish" button.

3.6) In the "Terms" section, left-click the "Add a property" drop-down below the
"0003-TEST" term, and select `rdfs:label`. In the resulting form,
enter `Test Label`, and left-click the "Save" button. Verify that:

* the term is updated to display the "rdfs:label" property
* at the top of the page there is a "Publish Updates" button, next to the
  "Unpublish" button

Left-click the "Publish Updates" button. Verify that the "Publish Updates"
button is removed.

### 4) Vocabularies Page

4.1) Left-click the "Vocabularies" entry in the navigation bar, and verify that
the "Vocabularies" page is displayed.

Verify that the page contains a table with a "Grove-Test" entry with the
following values (there will likely be other entries in the table):

* Label: `Grove-Test`
* Preferred Prefix: `test`
* Term Count: `3`
* URI: `http://example.com/grove-test#`

Verify that there is also a "Preview" column with following options:

* JSON-LD
* Turtle
* RDF/XML
* N-Triples

and a "Delete" button for the entry.

Verify that the page also contains a "Create Vocabulary" section with a form.

4.2) Left-click the `Turtle` option in the "Preview" column for "Grove-Test".
Verify that a page showing the "Grove-Test" vocabulary in RDF 1.1 Turtle
format is displayed as plain text. Left-click the browser's "Back" button to
return to the "Vocabularies" page.

4.3) In the "Create Vocabulary" section, enter `http://example.com/foobar#` in
the "URI" field, and left-click the "Add Vocabulary" button. Verify that a
"Vocabulary: Foobar" page is displayed.

4.4) Left-click the "Vocabularies" entry in the navigation bar. On the
"Vocabularies" page, verify that there is now a "Foobar" entry in the table.

4.5) Delete the "Foobar" entry in the table by left-clicking the "Delete"
button. After left-clicking the "OK" button in the confirmation dialog,
verify that the entry is removed from the table.

### 5) Predicates Page

5.1) Left-click the "Predicates" link in the navigation bar. Verify that the
"Predicate" page is displayed.

5.2) On the "Predicates" page, verify that there is a table of predicates with
the following columns:

* CURIE
* URI
* Object Type
* Usage Count

as well as a "Create Predicate" section with a form.

**Note:** It is currently not possible to delete a predicate, so creating
a predicate will not be tested.

### 6) Prefixes Page

6.1) Left-click the "Prefixes" link in the navigation bar. Verify that the
"Prefixes" page is displayed.

6.2) On the "Prefixes" page, verify that there is a table of prefixes with
the following columns:

* Prefix
* URI

### 7) Vocabulary Deletion

7.1) Left-click the "Vocabularies" link in the navigation bar. The
"Vocabularies" page will be shown.

7.2) On the "Vocabularies" page, left-click the "Delete" button for the
"Grove-Test" entry. After left-clicking the "OK" button in the confirmation
dialog, verify that the entry is removed from the table.

### 8) Logout

8.1) Left-click the "Logout" link in the navigation bar. Verify that the
CAS signout page is displayed.

8.2) In a web browser, go to

<https://grove-test.lib.umd.edu/>

Verify that the Grove home page with the "Log In" button is displayed.
