<br/>
<div align="center">
  <a href="https://github.com/PdgarHern/ReactWithRubyUsingPostregSQL">
    <img src="imgs/odoo_logo.png" alt="Logo" width="400" />
  </a>
  <h3 align="center">Anime Odoo module</h3>
  <br/>
</div>

<details>
  <summary>Index</summary>
  <ol>
    <li>
      <a href="#odoo-custom-module">Odoo Custom Module</a>
      <ul>
        <li><a href="#requirements">Requirements</a></li>
      </ul>
    </li>
    <li>
      <a href="#how-it-works">How it works</a>
    </li>
  </ol>
</details>

# Odoo Custom Module
Welcome to my Odoo custom module.<br/>
<br/>
My job was to create a module about the same topic and with the same functionalities as another project that I was doing.<br/>
(See the other project <a href="https://github.com/PdgarHern/ReactWithRubyUsingPostregSQL">here</a>)<br/>
<br/>
For this project I also had some requirements to match. So let me explain a bit how all works.<br/>

### Requirements
<ol>
  <li>New classes for the new module.</li>
  <li>New views for the new module.</li>
  <li>Inherited classes from other Odoo module existing class.</li>
  <li>Inherited views in other views already existing from other Odoo module.</li>
  <li>Actions, Menu elements and Group Rights.</li>
  <li>Inclusion of One2many and Many2one fields.</li>
  <li>Adapt some Odoo module functionality to the new module.</li>
  <li>Workflow creation</li>
  <li>Some personal addition to the module</li>
</ol>

# How it works
First, we have to install the module.<br/>
<div align="center">
  <img src="imgs/install.png" alt="install" widht="600" />
</div>

###
This will not just install our module, it will also install another modules like *Project* or *Invoicing* that we'll need to use our module.<br/>
<div align="center">
  <img src="imgs/modules.png" alt="modules" />
</div>

###
When you first enter the *Animes* module, you'll be in *anime*.<br/>
So, let's create a new one.<br/>
<div align="center">
  <img src="imgs/newAnime.png" alt="newAnime" width="600" />
</div>

###
Now, you may start to notice a few things.<br/>
Here, I've integrated a *mail box* from Odoo. This is made to match two of the requirements:
<ol>
  <li>Integrate an existing Odoo functionality</li>
  <li>The workflow</li>
</ol>
<div align="center">
  <img src="imgs/mailBox.png" alt="mailBox" />
</div>

###
So, if we hit the *Save* button a message (an activity, actually) will appear to the *Administrator* user.
<div align="center">
  <img src="imgs/workflow.png" alt="workflow" />
</div>

###
With an *anime* created, we now can create *actors* and *characters* associated to that *anime*.<br/>
Both can be created the same two ways:
<ol>
  <li>From the anime itself.</li>
  <!-- <ul></ul> -->
  <div align="center">
    <img src="/imgs/cAdd1.png" alt="cAdd1" width="600" />
  </div>
  <li>Going to its own page.</li>
  <div align="center">
    <img src="/imgs/cGo.png" alt="cGo" width="600" />
    <img src="/imgs/cAdd2.png" alt="cAdd2" />
  </div>
</ol>

###
Either way, you'll end up with the same result.
<div align="center">
  <img src="imgs/animeC.png" alt="animeC" width="600" />
  <img src="imgs/character.png" alt="character" width="300" />
</div>
