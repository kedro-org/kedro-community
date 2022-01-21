---
layout: image
image: background.png
---

<p class="text-2em text-yellow-500"><span class="bg-dark-900 m-2 rounded bg-opacity-60"> Open Kedro Retro #1 </span></p>

### June 2021

<div grid="~ cols-2 gap-4">
<div class="pt-12">
<p class="">
  <span @click="$slidev.nav.next" class="p-2 rounded cursor-pointer bg-dark-900 m-2 bg-opacity-60" hover="bg-white bg-opacity-10">
    Press <kbd>space</kbd> for next page <carbon:arrow-right class="inline"/>
  </span>
  </p>
  <div abs class="abs-bl ml-5 text-gray-500"><p class="text-xs">Best viewed in Dark mode, set it here:  <SetDarkMode/></p></div>
</div>
<div class="w-130"><KedroIcon /></div>

</div>


---
theme: apple-basic
class: text-left
highlighter: shiki
layout: iframe-right
url: https://github.com/kedro-org/kedro-viz
---

# Today's agenda

We’re excited to show you some of the cool stuff we’re currently cooking up and our vision for the future and Kedro's place within the ML ecosystem.

<ul>
  <li><span @click="$slidev.nav.go(11)" hover="bg-white bg-opacity-10 rounded">🤖 Meet the team</span></li>
  <li><span @click="$slidev.nav.go(2)"  hover="bg-white bg-opacity-10 rounded">🤔 What actually is Kedro?</span></li>
  <li><span @click="$slidev.nav.go(12)" hover="bg-white bg-opacity-10 rounded">👩‍🍳 What have the team been cooking?</span></li>
  <li><span @click="$slidev.nav.go(13)" hover="bg-white bg-opacity-10 rounded">🗑 No context Kedro </span></li>
  <li><span @click="$slidev.nav.go(15)" hover="bg-white bg-opacity-10 rounded">💅 Kedro Viz: Not just a pretty face</span></li>
  <li><span @click="$slidev.nav.go(16)" hover="bg-white bg-opacity-10 rounded">🔮 A look to the future</span></li>
  <li><span @click="$slidev.nav.go(22)" hover="bg-white bg-opacity-10 rounded">👋 Community improvements </span></li>
  <li><span>📣 Q&A</span></li>
</ul>

<Socials />

---

# Meet the team


<div class="flex">
  <div class="p-1">
    <div><h3>Framework team</h3></div>
    <div class="flex p-2 gap-3">
      <div><Profile name="Ivan" role="Tech lead" github="idanov" country="🇧🇬"/></div>
      <div><Profile name="Lorena" role="SWE" github="lorenabalan" country="🇷🇴"/></div>
      <div><Profile name="Merel" role="SWE" github="MerelTheisenQB" country="🇳🇱"/></div>
      <div><Profile name="Antony" role="DS SWE" github="AntonyMilneQB" country="🇬🇧"/></div>
      <div><Profile name="Ignacio" role="DS SWE" github="ignacioparicio" country="🇪🇸"/></div>
      <div><Profile name="Jiri" role="DE SWE" github="jiriklein" country="🇨🇿"/></div>
    </div>
  </div>

  <div class="p-1">
    <div><h3>Design team</h3></div>
    <div class="flex p-2 gap-3">
      <div><Profile name="Gabriel" role="Visual Designer"  country="🇧🇷" github="GabrielComymQB"/></div>
      <div><Profile name="Hamza" role="Design Research" github="hamzaoza" country="🇬🇧 🇵🇰"/></div>
    </div>
  </div>
</div>

<div class="flex">
  <div class="p-1">
    <div><h3>Viz team</h3></div>
    <div class="flex p-2 gap-3">
      <div><Profile name="Lim" role="Viz tech lead" github="limdauto" country="🇻🇳"/></div>
      <div><Profile name="Liam" role="Front end" github="bru5" country="🇬🇧"/></div>
      <div><Profile name="Susanna" role="Front end" github="studioswong"
      country="🇭🇰 🇦🇺"/></div>
      <div><Profile name="Rashida" role="Front end" country="🇮🇳" github="rashidakanchwala"/></div> 
    </div>
  </div>

  <div class="p-1">
    <div><h3>Product</h3></div>
    <div class="flex p-2 gap-3">
      <div><Profile name="Yetu" role="Product Lead" github="yetudada" country="🇿🇦"/></div>
      <div><Profile name="Joel" role="Product" github="datajoely" country="🇬🇧"/></div>
      <div><Profile name="Jo" role="Tech Writer" github="stichbury" country="🏴󠁧󠁢󠁷󠁬󠁳󠁿"/></div>
    </div>
  </div>
</div>


<Socials />


---
layout: image-right
---
<Overview />
<Socials />
<Youtube abs class="abs-tr mr-10 mt-30 rounded-xl" id="JLTYNPoK7nw" width="450" height="250"/>
---
layout: iframe-right
url: https://kedro.readthedocs.io/en/stable/02_get_started/06_starters.html
---
<Overview />
<Pointer class="absolute bottom-63"/>
<Speaker name="Joel"/>
<Socials />
---
layout: iframe-right
url: >-
  https://kedro.readthedocs.io/en/stable/05_data/01_data_catalog.html#using-the-data-catalog-with-the-yaml-api
---
<Overview />
<Speaker name="Joel"/>
<Pointer class="absolute bottom-55"/>
<Socials />
---
layout: iframe-right
url: https://kedro.readthedocs.io/en/stable/06_nodes_and_pipelines/01_nodes.html#how-to-create-a-node
---
<Overview />
<Speaker name="Joel"/>
<Pointer class="absolute bottom-47"/>
<Socials />
---
layout: iframe-right
url: https://kedro.readthedocs.io/en/stable/06_nodes_and_pipelines/02_pipeline_introduction.html#how-to-build-a-pipeline
---
<Overview />
<Speaker name="Joel"/>
<Pointer class="absolute bottom-40"/>
<Socials />
---
layout: iframe-right
url: https://kedro.readthedocs.io/en/stable/09_development/03_commands_reference.html#kedro-commands
---
<Overview />
<Speaker name="Joel"/>
<Pointer class="absolute bottom-32"/>
<Socials />
---
layout: iframe-right
url: https://kedro.readthedocs.io/en/stable/10_deployment/01_deployment_guide.html#deployment-choices
---
<Overview />
<Speaker name="Joel"/>
<Pointer class="absolute bottom-24"/>
<Socials />
---
layout: iframe-right
url: https://github.com/kedro-org/kedro-viz
---
<Overview />
<Pointer class="absolute bottom-16"/>
<Socials />
---

## What have the team been cooking recently 👩‍🍳?

 <Speaker name="Joel"/>

<h3> Recently, we have rewritten how Kedro works behind the scenes <ic-baseline-auto-fix-high class="inline"/><br>Since December 2020 🎄 we have released versions <kbd>0.17.0</kbd>, <kbd>0.17.1</kbd>, <kbd>0.17.2</kbd>, <kbd>0.17.3</kbd> and <kbd>0.17.4</kbd></h3>
<div class="grid grid-cols-4 mt-3">

  <div class="w-50 m-2">
    <div class="bg-dark-500 rounded-lg flex flex-col content-between  ">
      <emojione-building-construction class="text-3em m-auto mt-2 -mb-2 h-10"/>
      <p class="text-center text-0.8em">
        Rewritten framework internals
      </p>
    </div>
  </div>

  <div class="w-50 m-2">
    <div class="bg-dark-500 rounded-lg flex flex-col content-between ">
      <fxemoji-tapecartridge class="text-3em m-auto mt-2 -mb-2 h-10"/>
        <p class="text-center text-0.8em">
          <kbd>KedroSession</kbd> introduced
        </p>
    </div>
  </div>

  <div class="w-50 m-2">
    <div class="bg-dark-500 rounded-lg flex flex-col content-between ">
        <twemoji-sleeping-face class="text-3em m-auto mt-2 -mb-2 h-10"/>
        <p class="text-center text-0.8em">
          Lazy <kbd>Pipeline</kbd> loads
      </p>
    </div>
  </div>

  <div class="w-50 m-2">
    <div class="bg-dark-500 rounded-lg flex flex-col content-between">
      <la-cash-register class="text-3em m-auto mt-2 -mb-2 h-10 text-pink-400"/>
        <p class="text-center text-0.8em">
          Pipeline registry
        </p>
    </div>
  </div>

</div>


<div class="grid grid-cols-4">
  <div class="w-50 m-2">
    <div class="bg-dark-500 rounded-lg flex flex-col content-between ">
     <simple-icons-fastapi class="text-3em m-auto mt-2 -mb-2 h-10 text-green-400"/>
        <p class="text-center text-0.8em">
          FastAPI Viz backend
        </p>
    </div>
  </div>

  <div class="w-50 m-2">
    <div class="bg-dark-500 rounded-lg flex flex-col content-between ">
      <simple-icons-plotly class="text-3em m-auto mt-2 -mb-2 h-10 text-purple-400"/>
        <p class="text-center text-0.8em">
          Plotly dataset 
        </p>
    </div>
  </div>

  <div class="w-50 m-2">
    <div class="bg-dark-500 rounded-lg flex flex-col content-between">
      <dashicons-media-code class="text-3em m-auto mt-2 -mb-2 h-10 text-blue-200"/>
      <p class="text-center text-0.8em">
        Code panel
      </p>
    </div>
  </div>

  <div class="w-50 m-2">
    <div class="bg-dark-500 rounded-lg flex flex-col content-between ">
     <vaadin-file-tree-sub class="text-3em m-auto mt-2 -mb-2 h-10 text-yellow-400"/>
        <p class="text-center text-0.8em">
          Visual modular pipelines
        </p>
    </div>
  </div>

</div>

<div class="grid grid-cols-4">
  <div class="w-50 m-2">
    <div class="bg-dark-500 rounded-lg flex flex-col content-between ">
    <file-icons-jinja class="text-3em m-auto mt-2 -mb-2 h-10 text-red-400"/>
      <p class="text-center text-0.8em">
        Jinja2 templating
      </p>
    </div>
  </div>

  <div class="w-50 m-2">
    <div class="bg-dark-500 rounded-lg flex flex-col content-between ">
      <fxemoji-present class="text-3em m-auto mt-2 -mb-2 h-10 text-green-400"/>
        <p class="text-center text-0.8em">
          Improved packaging
        </p>
    </div>
  </div>

  <div class="w-50 m-2">
    <div class="bg-dark-500 rounded-lg flex flex-col content-between">
     <carbon-terminal class="text-3em m-auto mt-2 -mb-2 h-10 text-gray-100"/>
        <p class="text-center text-0.8em">
          Extensible CLI commands
        </p>
    </div>
  </div>

  <div class="w-50 m-2">
    <div class="bg-dark-500 rounded-lg flex flex-col content-between ">
      <emojione-bug class="text-3em m-auto mt-2 -mb-2 h-10"/>
        <p class="text-center text-0.8em">
          Dead bugs
        </p>
    </div>
  </div>

</div>


<Socials />


---

# No context Kedro ?

<Speaker name="Lorena"/>

<div class="">
<v-click>

- <carbon-clean class="inline text-yellow-500"/> In the beginning there was no context
- <carbon-crop class="inline text-yellow-500"/> Then the `KedroContext` helped us simplify Kedro
- <carbon-maximize class="inline text-yellow-500"/> Over time it has become too big and too bloated (esp. <kbd>IPython</kbd> / <vscode-icons-file-type-jupyter class="inline"/> sessions)
- 😭 It's now time to start divorce proceedings and move to a new approach
- <mdi-robot-dead class="inline text-yellow-500"/> In <kbd>0.18.0</kbd>  the already deprecated parts of the context will be removed entirely

</v-click>
</div>


---

# No context Kedro ?

<Speaker name="Lorena"/>

<div class="opacity-4">

- <carbon-clean class="inline text-yellow-500"/> In the beginning there was no context
- <carbon-crop class="inline text-yellow-500"/> Then the `KedroContext` helped us simplify Kedro
- <carbon-maximize class="inline text-yellow-500"/> Over time it has become too big and too bloated (esp. <kbd>IPython</kbd> / <vscode-icons-file-type-jupyter class="inline"/> sessions)
- 😭 It's now time to start divorce proceedings and move to a new approach
- <mdi-robot-dead class="inline text-yellow-500"/> In <kbd>0.18.0</kbd>  already deprecated parts of the context will be removed entirely

</div>

<div v-click class="abs abs-tl ml-36 mt-35"><Frame src="delorean.gif"/></div>

<div class="grid grid-cols-3 p-1">
<div class="border border-dark-400 rounded-lg py-2 content-between m-3">
<p class="text-center font-mono">KedroSession <carbon-logo-python class="inline" /></p>

<div class="text-sm">

- Introducing a <feather-database class="inline text-yellow-500"/>  store
- Deprecates the Journal <carbon-trash-can class="inline text-yellow-500"/>
- Time-travel superpowers <noto-superhero-medium-dark-skin-tone class="inline"/> 

</div>

</div>

<div v-click class="border border-dark-400 rounded-lg py-2 content-between m-3">
<p class="text-center font-mono">settings.py <file-icons-config-python class="inline" /></p>

<div class="text-sm">

- The recipe for a run <mdi-chef-hat class="inline text-yellow-500"/>
- <el-home-alt class="inline text-yellow-500"/> for project customisations
- <ri-caravan-fill class="inline text-yellow-500"/> `DataCatalog` is moving too...

</div>
</div>
<div v-click class="abs abs-tl ml-109 mt-35"><Frame src="recipe.gif"/></div>

<div v-click class="border border-dark-400 rounded-lg py-2 content-between m-3">
<p class="text-center font-mono">pyproject.toml <grommet-icons-document-config class="inline" /></p>

<div class="text-sm">

- <carbon-logo-python class="inline text-yellow-500"/> winds are changing...
- Kedro directory detection <carbon-terminal class="inline text-yellow-500"/>
- <el-home-alt class="inline text-yellow-500"/> for packaging spec in the future
</div>

</div>

<div v-click class="abs abs-tl ml-180 mt-35"><Frame src="packaging.gif"/></div>
</div>

<v-click>

<div>

```ini
kedro.framework.session.store - INFO - 'read()' not implemented for 'BaseSessionStore'. Assuming empty store
```
<p class="text-sm"><span class="animate-pulse">☝️</span> This annoying message will soon disappear!</p>

</div>

</v-click>

<Socials />

---
layout: quote
---

# 💅 Kedro Viz: Not just a pretty face

Also - we've just posted this [neat guide](https://github.com/kedro-org/kedro-viz/blob/main/LAYOUT_ENGINE.md)  to how our layout engine works
<div abs class=" abs-tr mr-25 mt-45">
<img src="/showtime.gif" class="rounded rounded-lg shadow-lg h-50"/>
</div>
<Speaker name="Susanna"/>

<Socials />

---
layout: quote
---
# 🔮 A look to the future 

<v-clicks>

- 👩‍🔬 Experiment tracking
- 🎁 Packaging modular pipelines
- ⏱ Diffing with Dolt
- ⚙️ Configuration optimisation

</v-clicks>

<Speaker name="Joel"/>
<Socials />

---

# 🧪 Native experiment tracking is coming to Kedro!

<div v-click>
<h3 class='p-2 m-3 opacity-100'><span class="p-1 bg-dark-500 rounded text-green-600 mr-2"><carbon-checkmark-filled class="inline text-green-600 mr-1"/>IN PROGRESS</span>User research phase</h3>

<div grid="~ cols-3 gap-4">
<div class="relative max-w-60 overflow-hidden rounded-lg shadow-lg">
  <img class="object-cover w-full h-22" src="/exp_a.png"/>
  <div class="absolute top-0 left-0 px-6 py-4">
  </div>
</div>

<div class="relative max-w-60 overflow-hidden rounded-lg shadow-lg">
  <img class="object-cover w-full h-22" src="/exp_b.png"/>
  <div class="absolute top-0 left-0 px-6 py-4">
  </div>
</div>

<div class="relative max-w-60 overflow-hidden rounded-lg shadow-lg">
  <img class="object-cover w-full h-22" src="/exp_c.png"/>
  <div class="absolute top-0 left-0 px- py-4">
  </div>
</div>
</div>

</div>

<div v-click>
<h3 class='p-2 m-3 opacity-100 animate-pulse'><span class="p-1 bg-dark-500 rounded text-yellow-500 mr-2"> <carbon-progress-bar-round class="inline text-yellow-500"/> IN PROGRESS</span>Discovery Phase</h3>

<div grid="~ cols-3 gap-4">
<div class="relative max-w-60 overflow-hidden rounded-lg shadow-lg">
  <img class="object-cover w-full h-22" src="/exp_d.png"/>
  <div class="absolute top-0 left-0 px-6 py-4">
  </div>
</div>

<div class="relative max-w-60 overflow-hidden rounded-lg shadow-lg">
  <img class="object-cover w-full h-22" src="/exp_e.png"/>
  <div class="absolute top-0 left-0 px-6 py-4">
  </div>
</div>

<div class="relative max-w-60 overflow-hidden rounded-lg shadow-lg">
  <img class="object-cover w-full h-22" src="/exp_f.png"/>
  <div class="absolute top-0 left-0 px-6 py-4">
  </div>
</div>

</div>
</div>

<div v-click>
<h3 class='p-2 m-3 opacity-100'><span class="p-1 bg-dark-500 rounded mr-2"><carbon-calendar class="inline"/>PENDING</span>Implementation Phase</h3>

<ul class="text-sm">
<li>Focus will be on <span class="text-yellow-500">the journey to production</span> <b>NOT</b> live model monitoring</li>
<li class="object-contain">Will integrate with <img src="/mlflow.png" class="object-contain h-8 inline border rounded p-2 ml-1 mr-1"/> model-registry</li>
</ul>
</div>
<Socials />
<Speaker name="Merel"/>


---

# Modular pipeline packaging


Our first iteration of our 'modular pipelines' feature (v0.16.2). 

<v-click>

- Users can <kbd>package</kbd>, <kbd>share</kbd>, <kbd>reuse</kbd> and <kbd>consume</kbd> pipelines as discrete units across teams. 
- We now have a year's worth of user feedback on where to take this next
- Ever-growing central `requirements.txt` is a common pain point

</v-click>

<v-click>
  <p class="text-gray-500">Inner-sourced knowledge</p>
  <p class="text-s">We want it to become common practice to re-use entire pipelines across different use cases.</p>
</v-click>

<v-click>
<div grid="~ cols-3 "><div class="flex flex-col border rounded m-1  border-dark-400">
    <div class="m-auto">
      <KedroIcon class="h-max vertical-center rounded-full bg-dark-500 m-3"/>
    </div>
  </div>
    <div class="flex flex-col border rounded m-1 border-dark-400">
    <div class="m-auto text-center">
      <Arrow x1=600 y1=470 x2=380 y2=470 class="text-yellow-500 text-xl animate-pulse"/>
      <p>Push pipelines</p>
      <p>Pull source code</p>
      <Arrow x1=380 y1=360 x2=600 y2=360 class="text-yellow-500 text-xl animate-pulse"/>
    </div>
  </div>
  <div class="flex flex-col border rounded m-1 border-dark-400">
    <div class="m-auto mt-2">    
      <span>
        <simple-icons-jfrog class="m-2 h-6 w-6 text-green-400 inline"/>
        <p class="inline text-xs">JFrog Artifactory</p>
      </span>
      <br>
      <span>
        <file-icons-pypi class="m-2  h-6 w-6 text-indigo-400 inline"/>
        <p class="inline text-xs">PyPI</p>
      </span>
      <br>
      <span>
        <mdi-azure-devops class="m-2  h-6 w-6 text-blue-500 inline"/>
        <p class="inline text-xs">Azure Artifacts</p>
      </span>
      <p class="text-xs text-gray-300 text-center">Any PyPI like endpoint</p>
    </div>
  </div>
</div>
</v-click>


<Speaker name="Lim"/>
<Socials />


---

# Diffing with Dolt (1/2)
<Speaker name="Dolt team"/>

<div class="flex">

  <div class="flex-grow">
    <div><Profile name="Max" role="Integrations Engineer" github="max-hoffman" class="mb-3"/></div>
    <div><Profile name="Oscar" role="Product" github="oscarbatori"/></div>
  </div>
  <div class="flex-auto"> 
  

  <img src="/kedro-retro-june-2021/dolt_team.png" class="h-30 m-auto">

  <ul class="text-0.8em max-w-80">
  <li>Dolt is database you can use like <code>git</code> </li>
  <li>Takes versioning to the next level </li>
  <li>Supports crazy stuff like data <code>diff</code> 🤯</li>
  <li>Python API, CLI or SQL interface</li>
  <li>Seamless Kedro <KedroIcon class="h-8 inline"/> integration is coming!</li>
  </ul>
    
</div>
<div class="flex-shrink">

```bash 
$ dolt diff
diff --dolt a/state_populations b/state_populations
--- a/state_populations @ qqr3vd0ea6264oddfk4nmte66cajlhfl
+++ b/state_populations @ 17cinjh5jpimilefd57b4ifeetjcbvn2
+-----+---------------+------------+
|     | state         | population |
+-----+---------------+------------+
|  <  | New Hampshire | 0          |
|  >  | New Hampshire | 141885     |
|  <  | New Jersey    | 0          |
|  >  | New Jersey    | 184139     |
|  <  | New York      | 0          |
|  >  | New York      | 340120     |
+-----+---------------+------------+

$ dolt
```

<div abs class="abs-tl mt-90 ml-137"><p class="animate-pulse token function font-mono"> | </p></div>
</div>
</div>
<br>

Access the Dolt discord [here](https://discord.gg/s8uVgc3) <carbon-logo-discord class="inline"/>
<Socials />


---

# Diffing with Dolt (2/2)
<Speaker name="Dolt team"/>

<div class="flex">

  <div class="flex-grow">
    <div><Profile name="Max" role="Integrations Engineer" github="max-hoffman" class="mb-3"/></div>
    <div><Profile name="Oscar" role="Product" github="oscarbatori"/></div>
  </div>
  <div class="flex-auto"> 

  <div class="m-2">    
    <h3>Dolt</h3>
    <ul>
    <li>SQL query interface - (99%) MySQL compliant</li>
    <li>Git-like features - efficient <code>branch</code>, <code>diff</code>, <code>merge</code></li>
    <li>Repo isolation - <code>clone</code>, <code>push</code>, <code>pull</code></li>
    </ul>
  </div>
  
  <div class="m-2">  
    <h3>Diffs</h3>
    <ul>
    <li>Viz tools are increasingly complex - drift, validations, embeddings</li>
    <li>Diffing is simple, crude, and effective</li>
    <li>Diffs exposed via SQL tables for automating validation of data changes</li>
    <li>Source code diff <carbon-arrow-right class="inline text-yellow-500"/> view state changes</li>
    <li>Database diff <carbon-arrow-right class="inline text-yellow-500"/> view state changes</li>
    </ul>
  </div>

</div>
</div>

Access the Dolt discord [here](https://discord.gg/s8uVgc3) <carbon-logo-discord class="inline"/>

<Socials />

---

# Config optimisation



<div class="flex pb-4">
<v-click at='4'><img abs src="/help.png" class="rounded-xl abs-tr h-55 mr-25 mt-56"/></v-click>
<v-click at="1">

<div class="flex-1">

  <div class="text-sm">

  ### Configuration complexity is increasing 

  - We designed against the principles of the [12 factor app](https://12factor.net/config)
  - Large Kedro projects generate a lot of YAML
  - There is no IDE support for bad YAML or references 

  </div>


</div>
</v-click>

<div class="flex mr-4">

<v-click at="3">
<div class="text-sm inline">

### What have our users have been saying?
 
- Can I have a dynamically generated catalog?
- How do I parameterise a complex run?
- Help I'm drowning in YAML!

</div>
</v-click>
</div>
</div>

<v-click at="2">
<div class="text-sm w-124">

### Over time bandaid fixes <gg-band-aid class="inline text-pink-500"/> have been introduced:


|||
|---|---|
|YAML <code>&anchors</code> for reusing common structures|<div class="inline bg-dark-500 m-2 pl-1 pr-2 rounded-lg text-xs"><carbon-arrow-up class="inline text-green-400" /> brevity <carbon-arrow-down class="inline text-red-500" /> readability</div>|
|<code>run environments</code> allowing staging, test, prod patterns|<div class="inline bg-dark-500 m-2 pl-1 pr-2 rounded-lg text-xs"><carbon-arrow-up class="inline text-green-400" /> customisation <carbon-arrow-down class="inline text-red-500" /> brevity</div>|
|<code>TemplatedConfigLoader</code> DSL for string interpolation|<div class="inline bg-dark-500 m-2 pl-1 pr-2 rounded-lg text-xs"><carbon-arrow-up class="inline text-green-400" /> brevity <carbon-arrow-down class="inline text-red-500" /> readability</div>|
|<code>jinja2</code> introduces loops, conditionals and more|<div class="inline bg-dark-500 m-2 pl-1 pr-2 rounded-lg text-xs"><carbon-arrow-up class="inline text-green-400" /> dynamism <carbon-arrow-down class="inline text-red-500" /> readability</div>|

</div>
</v-click>

<Speaker name="Joel"/>
<Socials />


---

# Community improvements

<Speaker name="Yetu"/>


<div grid="~ cols-2 gap-4">
    <div>
        <div v-click class="mb-12">
            <div class="flex">
                <div class="flex-1">
                    <p class="text-gray-500 text-sm inline">
                        Slide into our DMs on
                    </p>
                    <p class="inline bg-indigo-400 text-black p-1 rounded font-mono text-xs inline">
                        Discord
                        <carbon-logo-discord class="inline" />
                    </p>
                    <p class="text-sm">
                        Open forum to chat
                        <carbon-chat-bot class="inline" />
                        with the dev team and for the community to assist support each other
                        <carbon-help class="inline" />
                    </p>
                </div>
                <div class=""><img src="/discord_qr.svg" class="w-25 mb-3 ml-3 mr-6 rounded" /></div>
            </div>
              <iframe src="https://discord.com/widget?id=778216384475693066&theme=dark" width="400" height="220" allowtransparency="true" frameborder="0" sandbox="allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts"></iframe>
        </div>
    </div>
        <div class="object-center">
            <div v-click class="">
                <p class="text-sm text-gray-500"></p>
                <p class="inline bg-gray-300 text-black p-1 rounded font-mono text-xs">
                    GitHub Discussions
                    <carbon-logo-github class="inline m-1" />
                </p>
                <p class="inline"> will help codify knowledge 🙌</p>
                <p class="text-sm">
                    Threaded conversations
                    <twemoji-thread class="inline" />
                    , answers marked by the maintainer
                    <carbon-checkmark-filled class="inline text-green-400" /> <br />
                    and pinned announcements
                    <carbon-pin-filled class="inline text-pink-500" />
                </p>
                <table class="tg">
                    <thead>
                        <tr>
                            <td class="tg-0pky">🙌</td>
                            <td class="tg-0pky"><span style="font-style: normal;">Show and tell</span></td>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="tg-0lax">💡</td>
                            <td class="tg-0lax">Ideas</td>
                        </tr>
                        <tr>
                            <td class="tg-0lax">🙏</td>
                            <td class="tg-0lax">Q&amp;A</td>
                        </tr>
                        <tr>
                            <td class="tg-0lax">🆘</td>
                            <td class="tg-0lax">Help</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        <div v-click class="mt-5">
            <p class="text-sm text-red-400 inline">
                Deprecation 😭 of
            </p>
            <p class="inline bg-red-400 text-black m-1 p-1 rounded font-mono text-xs">
                discourse.kedro.community
                <fa-brands-discourse class="inline" />
            </p>
            <p class="text-sm">
                We hope that the two avenues above will be better to this, StackOverflow
                <fa-brands-stack-overflow class="inline" />
                and other platforms
            </p>
        </div>
        <v-click>
            <div abs class="abs-tl w-screen h-screen flex bg-gradient-to-b from-dark-400 to-dark-900 opacity-90"></div>
            <div abs class="abs-tl mt-40 ml-40 ">
            <div><img src="/kedroid.png" class="transform -rotate-10 h-30 inline"></div>
            </div>
            <div abs class="abs-tl mt-47 ml-72 bg-dark-800 p-5 bg-opacity-80 rounded-1em">
              <p class="inline text-1em">Remember! Helpful </p>
              <p class="inline text-2.0em text-yellow-500 p-2">Kedroids</p>
              <p class="inline text-1em">get cool merch <KedroIcon class="inline h-9 align-top"/></p>
            </div>
        </v-click>
    </div>
    
</div>

<Socials />

---
layout: quote
---
# 📣 Open Q&A Session

<div abs class=" abs-tr mr-60 mt-52">
<img src="/questions.gif" class="rounded rounded-lg shadow-lg h-30"/>
</div>
<Socials />
