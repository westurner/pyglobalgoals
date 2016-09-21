
# coding: utf-8

# # Python for Linked Data: RDFS, RDFa, JSONLD, and Schema.org
# Developing a generalized RDFS Vocabulary for Goals, Objectives,
# Targets, and Indicators for the [UN](https://un.org) [Global Goals](http://globalgoals.org/)
# - | @type: CreativeWork > JupyterNotebook
# - | author: @westurner
# - | createdDate: 2016-09-19
# - | url: https://github.com/westurner/pyglobalgoals TODO
# 

# ## #GlobalGoals for Sustainable Development (UN #SDGs)
# - https://globalgoals.org/
# - #GlobalGoals Week 2016: Sep 18 - 24th
# - The United Nations Sustainable Development Goals are the international
#   Goals, Targets, and Indicators for now through 2030. (#2030Now)
# 
# > "17 goals to achieve 3 extraordinary things in the next 15 years"
# >
# >  - End extreme poverty.
# >  - Fight inequality & injustice.
# >  - Fix climate change.
# 

# 
# [![The 17 Global Goals](https://media.globalcitizen.org/thumbnails/0a/8d/0a8da7a0-09c8-4298-8839-09673064b51c/global-goals-full-icons.png__2318x1180_q85_crop_subsampling-2_upscale.jpg)](https://media.globalcitizen.org/thumbnails/0a/8d/0a8da7a0-09c8-4298-8839-09673064b51c/global-goals-full-icons.png__2318x1180_q85_crop_subsampling-2_upscale.jpg)

# ## Objectives
# - Learn Linked Data Concepts
# - Define the Schema (SCH)
#   - SCH: schema.org/ :Project, :Goal, :Objective (un:Target), :Task, :Indicator,
#   - Extract the Data (DAT)
#     - pyglobalgoals Objectives
#       - https://github.com/westurner/pyglobalgoals/blob/develop/notebooks/globalgoals-pyglobalgoals.py.ipynb
# - Link Organizations' \[Projects'] \[Objectives] to un:GlobalGoals
#   - Query: "Show me Organizations with Projects relevant to e.g. #Goal3 'Climate Action' "
#   - Query: "Show me Performance.gov Goals relevant to e.g. #Goal3 'Climate Action' "
#   - Query: "Find solutions that are affecting [local] change in these []Indicators"

# ### Pessimistic, Optimistic, Realistic
# - Pessimistic
#   - Accomplish nothing more than existing KISS approaches
#   - Create work in evaluating Organizations' assertions (see: central SQL database)
# - Optimistic
#   - Make it easy to find organizations with similar objectives
# - Realistic
#   - Learn about Linked Data
#   - Produce a data interchange spec for further development
#   - Build/aggregate a catalog / directory / **graph** of GOs, NGOs, and [Non-] Profits

# ## Existing KISS solutions
# - KISS: Keep it Simple
# - search(engine, "#Goal3")
#   - "(They're / We're) working on #Goal3" # need for #LinkedData, #StructuredData
#     - A mention is not a structured Project/Goal/Objective relation
# - Tree/outline of Goals, Objectives and relevant Projects
#   - Denormalization ("We're working on goals 1, 2, and 3")
# - Central SQL Schema, Database, HTML Templates
#   - SQL Schema : RDFS Schema :: SQL Database : RDF Graph Database
#   - This could work, too
#     - But I just want to search with a search engine
#     - Nobody is going to login to your app to keep updating their directory entry
#     - Then I *still* want to aggregate a graph of resources from {websites, social networks}
#       - Global Goals App:
#         - http://www.globalgoals.org/globe/
#           - ~(schema:Person, un:GlobalGoal, schema:Location, schema:Image)
#         - http://www.globalgoals.org/2015/09/29/download-the-global-goals-app/
#         - Instagram, Facebook, Twitter (... https://schema.org/SocialMediaPosting )
# - http://indicators.report/indicators/ # Indicators by Goals

# ### For academic purposes
# - We assume that none of the Existing KISS solutions
#   completely solve for these additional objectives (user stories, use cases)
#   - (Or, that this academic exercise will produce new ideas for existing solutions)
#   - And forge ahead with implementing **#LinkedData** for the **#GlobalGoals**
#     - \[ ] Take a few days and build a different solution anyway; because better
# - What can we add to the existing solutions?
#   - Links between {performance.gov Goals, } and {GlobalGoals/SDGs, Indicatord}
#     - Where a 'link' is an RDF relation
#   - TIL this is called "strategic alignment"
#     https://en.wikipedia.org/wiki/Strategic_alignment
#     - StratML: https://en.wikipedia.org/wiki/Strategy_Markup_Language
#       - https://github.com/schemaorg/schemaorg/issues/1127#issuecomment-220780158

# #  Learn #LinkedData Concepts
# - Linked Data
#   - RDF
#     - RDFa
#     - JSONLD
#   - RDFS
#     - Schema.org
# 
# 
# 
# 
# 
# 

# ### Linked Data
# - https://wrdrd.com/docs/consulting/knowledge-engineering#linked-data
# - 5 Star Linked Data: http://5stardata.info
#   - ☆ Publish data on the Web in any format (e.g., PDF, JPEG) accompanied by an explicit Open License (expression of rights).
#   - ☆☆ Publish structured data on the Web in a machine-readable format (e.g. XML).
#   - ☆☆☆ Publish structured data on the Web in a documented, non-proprietary data format (e.g. CSV, KML).
#   - ☆☆☆☆ Publish structured data on the Web as RDF (e.g. Turtle, **RDFa**, **JSON-LD**, SPARQL.)
#   - ☆☆☆☆☆ In your RDF, have the identifiers be **[links]() (URLs)** to useful data sources.

# ### RDF
# - https://wrdrd.com/docs/consulting/knowledge-engineering#rdf
# - RDF (*Resource Description Format*) is a W3C Standard for **Graphs** of **Triples** (or *Quads*)
# - Triple: (Subject, Predicate, Object)
# - Quad: (Graph, Subject, Predicate, Object) # "Named Graph"
# - Graph, Subject, and Predicate SHOULD be URIs
#   - ([URI], URI, URI, Value)
# - An example with subject [#thing1]()
#   - ([#thing1](), a, [schema:CreativeWork](http://schema.org/CreativeWork)) ... "a" == rdf:Type
#   - (http://example.org/page, [#thing1](), a, [schema:CreativeWork](http://schema.org/CreativeWork))
#   - (http://example.org/page, [#thing1](), [schema:name](http://schema.org/name), "Thing 1"@en)
# - XSD Types (xsd:string, xsd:boolean, xsd:decimal, xsd:base64Binary)
#   - https://www.w3.org/TR/xmlschema11-2/#built-in-datatypes
# - ``"Hello World"@en`` has an ``xml:lang`` of "en" (Turtle syntax)
# - rdf:List for guaranteed ordering (*)

# #### Objectives (Turtle RDF Syntax)
# - [https://en.wikipedia.org/wiki/Turtle_(syntax)]()
# 
# ```turtle
# <> a schema:Project;
#   schema:name "Python for Linked Data: RDFS, RDFa, JSONLD, and Schema.org"@en ;
#   schema:description "Developing a generalized RDFS Vocabulary for Goals, Objectives,
# Targets, and Indicators for the UN Global Goals"@en ;
#   schema:hasPart [ 
#       a schema:Objective ;
#       schema:name "Learn Linked Data Concepts"@en ;
#       schema:hasPart [
#           a schema:Objective ;
#           schema:name "Define schema.org/ :Project, :Goal, :Objective (un:Target), :Task, :Indicator,"@en ;
#   ];
#   schema:hasPart [
#       a schema:Objective;
#       schema:name "Link Organizations' [Projects'] [Objectives] to un:GlobalGoals"@en ;
#       schema:hasPart [
#           a schema:Objective ;
#           schema:name "Query: \"Show me Organizations with Projects relevant to e.g. #Goal3 'Climate Action' ""@en ;
#       ]
#   ]
#   .
# ```

# ### RDFS
# - https://wrdrd.com/docs/consulting/knowledge-engineering#rdfs
# - RDFS ("RDF Schema") is a standard for specifying vocabularies of Classes with Properties.
# - Class (C)
#   - rdf:type schema:Thing # RDF
#   - @type: schema:Thing   # JSONLD
# - Property (P)
#   - rdfs:**domain** schema:Thing
#   - rdfs:**range** [schema:Text, schema:Thing, schema:URL]
# - Schema.org is an RDFS Vocabulary maintained as RDFa (and transformed to RDF/XML, Turtle, JSONLD)

# ### RDFa
# - https://wrdrd.com/docs/consulting/knowledge-engineering#rdfa
# - RDFa ("RDF in Attributes") is a W3C standard for inlining structured data in an (X)HTML(5) page.
# - HTML + extra attributes = RDFa
# - An example of adding RDFa to an HTML page
#   - https://github.com/CodeForAntarctica/codeforantarctica.github.io/pull/3/files
#   - TODO: screenshot?
# - Schema.org Core Vocabulary RDFa:
#   - https://github.com/schemaorg/schemaorg/blob/sdo-callisto/data/schema.rdfa

# ### JSON-LD
# - https://wrdrd.com/docs/consulting/knowledge-engineering#jsonld #JSONLD
# - JSON-LD (*JSON Linked Data*) is a W3C Standard for getting RDF triples from some or all of a JSON Document.
# - JSON + **``@context``** document = JSONLD
# - "JSON-LD and Why I Hate the Semantic Web" 
#   http://manu.sporny.org/2014/json-ld-origins-2/
#   - RDF can be frustrating for programmers
#   - Ordered lists in RDF require explicit ``rdf:first`` and ``rdf:rest`` constructions:
#   
#   > RDF is a s----- data model. It doesn’t have native support for lists. LISTS for f---’s sake! The key data structure that’s used by almost every programmer on this planet and RDF starts out by giving developers a big fat middle finger in that area.
#   
#   - JSON-LD supports lists
#   
#   ```json
#   { "@context": {
#       "listOfThings": { "@container": "@list", "@type": "string"},
#       "listOfURIs":   { "@container": "@list", "@type": "@id" } },
#     "listOfThings": ["one", "two", "three"],
#     "listOfURIs": ["http://#one", "http://#two", "http://#three"],
#   }
#   ```

# #### JSON-LD Schema.org Example 1 (@context URL)
# - An example: This meeting:
#   - https://schema.org/Event
#     - location: https://schema.org/Place
#       - address: https://schema.org/PostalAddress
# - A client MAY retrieve (and cache) the JSONLD @context(s)
#     
# ```json
# {"@context": ["http://schema.org/", {"schema": "http://schema.org/"}],
#  "@type": "Event",
#  "name": "Omaha Python Users Group September Meeting",
#  "url": "http://www.omahapython.org/blog/archives/501",
#  "startDate": "2016-09-21T18:30:00-0500",
#  "endDate": "2016-09-21T20:30:00-0500",
#  "location": {
#    "@type": "schema:Place",
#    "name": "DoSpace: Meeting Room 2",
#    "url": "http://dospace.org/",
#    "hasMap": "https://www.google.com/maps?daddr=7205+Dodge+Street+Omaha+NE",
#    "address": {
#      "@type": "schema:PostalAddress",
#      "addressCountry": "USA",
#      "postalCode": "68114",
#      "streetAddress": "7205 Dodge Street",
#      "addressLocality": "Omaha",
#      "addressRegion": "NE"
#    }
#  }
# }
# ```

# #### JSON-LD Schema.org Example 2 (inline @context)
# 
# ```json
# {"@context": ["http://schema.org/", {
#    "title": "http://schema.org/name",
#    "date_created": "http://schema.org/dateCreated",
#    "sameAs": { "@type": "@id", "@container": "@list" }
#  }],
#  "@graph": [
#    {"title": "Thing1",
#     "url": "#Thing1",
#     "date_created": "2016-09-19",
#     "sameAs": ["http://#Thing2", "https://#Thing3"],
#    }
#  ]
# }
# ```
# - [...] http://json-ld.org/playground/

# #### schema.org/sameAs JSON-LD
# - http://schema.org/sameAs  # Schema URIs are HTTP
# - https://schema.org/sameAs
# - https://raw.githubusercontent.com/schemaorg/schemaorg/sdo-callisto/data/releases/3.2/all-layers.jsonld
# 
# ```json
# {
#   "@id": "http://schema.org/sameAs",
#   "@type": "rdf:Property",
#   "http://schema.org/domainIncludes": {
#     "@id": "http://schema.org/Thing"
#   },
#   "http://schema.org/rangeIncludes": {
#     "@id": "http://schema.org/URL"
#   },
#   "rdfs:comment": "URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website.",
#   "rdfs:label": "sameAs"
# },
# ```
# - side note: schema:sameAs != owl:sameAs (``schema:sameAs owl:differentFrom owl:sameAs``)
#   - http://prefix.cc/owl:sameAs
#   - https://www.w3.org/TR/owl2-quick-reference/#Axioms
# ```turtle
#   owl:sameAs a rdf:Property ;
#      rdfs:label "sameAs" ;
#      rdfs:comment "The property that determines that two given individuals are equal." ;
#      rdfs:domain owl:Thing ;
#      rdfs:isDefinedBy <http://www.w3.org/2002/07/owl#> ;
#      rdfs:range owl:Thing . 
# ```

# ### Schema.org
# - | Homepage: https://schema.org/
# - https://wrdrd.com/docs/consulting/knowledge-engineering#schemaorg
# - Schema.org is a unified RDFS vocabulary for describing Thing(s) as RDFa, Microdata, JSON-LD
# - [Bing, Google, Yahoo, Yandex,] all index specific http://schema.org/Thing s
# - Schema.org RDFa: https://github.com/schemaorg/schemaorg/blob/sdo-callisto/data/schema.rdfa
#   - Schema.org JSONLD: https://github.com/schemaorg/schemaorg/blob/sdo-callisto/data/releases/3.2/all-layers.jsonld

# # Define the Schema
# 
# - [ ] SCH: Classes and Properties (Schema.org RDFS RDFa)
# - [ ] DAT: Examples (JSON-LD,)
#   - [ ] ETL Existing Data (Extract-Transform-Load)
# 

# ## SCH: Classes and Properties
# * | Issue: https://github.com/schemaorg/schemaorg/issues/1127
# * | Branch: https://github.com/westurner/schemaorg/tree/feature/mission-project-goal-objective-task
# * | PR: https://github.com/schemaorg/schemaorg/pull/1128
# - Classes
#   - [x] [CreativeWork](https://schema.org/CreativeWork)
#     - [-] Project
#     - [-] Goal
#     - [ ] Completeable
#       - [-] Objective (un:Target)
#       - [-] Task
#     - [ ] Indicator
#       - [StructuredValue](https://schema.org/StructuredValue), XKOS, W3C Data Cubes (``qb:``) is a superset of SDMX 
#       - [ ] QualitativeIndicator
#       - [ ] QuantitativeIndicator
# - Properties
#   - [x] [partOf](https://schema.org/partOf)
#   - [-] mission d:Organization r:Text 

# ## DAT: Examples
# - schema.org examples are stored in flat .txt files w/ custom record delimiters
#   - ``TYPES:``, ``PRE-MARKUP:``, ``MICRODATA:``, ``RDFA:``, ``JSON:`` (JSON-LD)
#   - https://github.com/schemaorg/schemaorg/blob/sdo-deimos/data/examples.txt
#   - https://github.com/schemaorg/schemaorg/tree/sdo-deimos/data/ext/pending
#     - ./issue-1127.rdfa
#     - ./**issue-1127-examples.txt**

# ### ETL Existing Data
# - The Global Goals (and SDGs) are available from various HTML pages
#   - http://www.un.org/sustainabledevelopment/sustainable-development-goals/
#     - [x] http://globalgoals.org/
#       - [ ] http://www.globalgoals.org/global-goals/no-poverty/ (sdg1)
#   - [ ] http://unstats.un.org/sdgs/metadata/ (Goal 1, Target 1.1, Indicator 1.1.1)
#   - [ ] https://sustainabledevelopment.un.org/sdgs
#     - [ ] https://sustainabledevelopment.un.org/sdg1
#   - [ ] http://unstats.un.org/sdgs/report/2016/
#     - [ ] http://unstats.un.org/sdgs/report/2016/goal-01/

# #### pyglobalgoals
# - BeautifulSoup( http://globalgoals.org/ ) => JSON-LD
# - https://github.com/westurner/pyglobalgoals/blob/develop/notebooks/globalgoals-pyglobalgoals.py.ipynb
#   - JSON-LD: https://github.com/westurner/pyglobalgoals/blob/develop/notebooks/data/globalgoals.jsonld
#     - [ ] g.parse(graph1); g.parse(graph2)  # implicit merge on @id

# # Link between different Goal sets
# - https://www.performance.gov/node/3406 "Climate Change (Federal Actions)"
# - Goal 13: http://www.globalgoals.org/global-goals/protect-the-planet/
#   - Goal 7: http://www.globalgoals.org/global-goals/modern-energy/
#   
# ```json
# [{"@type": "schema:Goal",
#   "name": "Climate Change (Federal Actions)",
#   "url": "https://www.performance.gov/node/3406",
#   "@id": "https://www.performance.gov/node/3406",
#   
#   "globalgoal": [
#       "http://schema.un.org/#Goal13",
#       "http://schema.un.org/#Goal7"
#    ]
# }]
# ```
# 
# - This is flat, simple property
#   - This relation could/should be reified as an Edge Class
#   
# ```json
# [ {"@type": "todo:GoalRelation",
#    "from": "https://www.performance.gov/node/3406",
#    "to": "http://schema.un.org/#Goal13",
#    "dateCreated": "...",
#    "author": "...",
#    "comments": [...]
#   }
# ]
# ```

# # Tools
# - Presentation
#   - Jupyter Notebook: https://wrdrd.com/docs/tools/#jupyter-notebook
#   - nbpresent: https://wrdrd.com/docs/tools/#nbpresent
# - Code
#   - conda: https://wrdrd.com/docs/tools/#conda
#   - rdflib: https://wrdrd.com/docs/consulting/knowledge-engineering#rdflib
#     - rdflib-jsonld: https://github.com/RDFLib/rdflib-jsonld
