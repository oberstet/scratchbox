# UI Stack & Tools Whitelist

The following is our handpicked, agreed list of libraries and tools to create rich HTML5-based frontends.

## Libs

1. Utils
 * Base: [HTML5 Boilerplate](http://html5boilerplate.com/)
 * DOM: [jQuery](http://jquery.com/)
 * Feature detection: [Modernizr](http://modernizr.com/)
 * Functional JS: [Underscore](http://underscorejs.org/)
 * URI processing: [URI.js](http://medialize.github.io/URI.js/)
 * Cryptography: [CryptoJS](http://code.google.com/p/crypto-js/)
 * Deferreds: [When](https://github.com/cujojs/when)
2. Core
 * **UI**: [jQuery Mobile](http://jquerymobile.com/)
 * **MVVM**: [Knockout](http://knockoutjs.com/)
 * **Communication**: [Autobahn](http://autobahn.ws/js)
3. Graphics 
 * Charts & 2D Visualization: [D3](http://d3js.org/)
 * 3D Visualization: [Three](http://threejs.org/)
4. Grids
 * Grid: [DataTables](https://datatables.net/)
 * Spreadsheet: [jQuery.sheet](http://visop-dev.com/Project+jQuery.sheet)
5. Misc
 * Syntax Highlighter: [SyntaxHighlighter](http://alexgorbatchev.com/SyntaxHighlighter/)
 * Code editor: [Ace](http://ace.c9.io/)

## Tools

1. Testing: [BusterJS](http://docs.busterjs.org/en/latest/)
2. Optimization: [UglifyJS](https://github.com/mishoo/UglifyJS2)
3. Automation: [Grunt](http://gruntjs.com/)
4. [Scaffolding](http://en.wikipedia.org/wiki/Scaffold_%28programming%29): [Jo](http://yeoman.io/)
5. Transpiling: [Less](http://lesscss.org/)
5. ... tbd 

## Others

* [Chrome DevTools](https://developers.google.com/chrome-developer-tools/)
* [Z](https://github.com/rupa/z)

# Notes

## Tools

In general, we want our toolchain be based on Node/npm and not requiring "additional" stuff like Java or Ruby.

### CSS Preprocessor

Less provides:

 * familiar CSS-like syntax
 * runs on Node/npm
 * widely used

Sass has alien syntax (from CSS POV). Scss requires Ruby.

Less integrates into Grunt:

 * [Here](https://github.com/gruntjs/grunt-contrib-less)
 * [Here](http://stackoverflow.com/questions/15664628/grunt-less-and-file-watching)
 * [Here](https://github.com/sindresorhus/grunt-recess)

## Tables, Grids and Spreadsheets

### Tables

For basic tables, we rely on jQuery Mobile widgets. These provide [reflow](http://view.jquerymobile.com/1.3.2/dist/demos/widgets/table-reflow/) and [column toggle](http://view.jquerymobile.com/1.3.2/dist/demos/widgets/table-column-toggle/).

### Grids

> Grids should only be used/necessary when a "simple" table is definitely not sufficient.

The grid data in our archiecture will exist in the ViewModel as an observable array of observable arrays. This ViewModel grid data is bound to a HTML table using Knockout.

For example, when adding a new row to the data within the ViewModel (e.g. upon receiving a PubSub event from the backend), Knockout will apply it's magic and create a new HTML `<tr>` table child element in the DOM. Now, what we need after that is *progressive enhancement* of the (generated) HTML.

Hence, we need a JS grid library that was built with *progressive enhancement* in mind.

There are dozens of JavaScript grid implementations. Of the ones used together with jQuery, it seems the most popular are: [jqGrid](http://jqgrid.com/), [Slickgrid](https://github.com/mleibman/SlickGrid) and [DataTables](https://datatables.net/).

Of those, only DataTables was natively designed for *progressive enhancement* and *semantic HTML*: a grid is based on enhancing a native HTML `<table>`. In other words: DataTables fits our MVVM pattern and [integrates](http://chadmullins.com/javascript/knockout-js-series-part-2-binding-knockout-js-to-a-datatables-grid/) with Knockout.

### Spreadsheets

A spreadsheet is more than an editable grid: it provides cell formulas.

I have looked at [jQuery.sheet](http://visop-dev.com/Project+jQuery.sheet), [SpreadJS](http://wijmo.com/widgets/wijmo-enterprise/spreadjs/), [dhtmlxSpreadsheet](http://www.dhtmlx.com/docs/products/dhtmlxSpreadsheet/) and [Handsontable](http://handsontable.com/demo/understanding_reference.html).

None of those can reproduce the Excel user experience. Not even the Google Docs UX.

Handsontable is quite snappy and looks slick, but does not support cell formulas.

However, jQuery.sheet is usable.

## Modules

In general, there are 2 approaches to modularity with JavaScript (browser) today:

 * AMD (Asynchronous Module Definition)
 * [CommonJS Modules](http://wiki.commonjs.org/wiki/Modules)

The single most widely deployed AMD implementation is [RequireJS]([RequireJS](http://requirejs.org/)).

Another AMD implementation that looks good is [curl](https://github.com/cujojs/curl). It [claims](https://github.com/cujojs/curl/wiki/Using-curl.js-with-CommonJS-Modules) to be able to use unwrapped CommonJS modules without compiling.


## Deferreds

 * [when](https://github.com/cujojs/when)
 * [jQuery Deferreds](http://api.jquery.com/jQuery.Deferred/)


## Code Minification and Obfuscation

 * [Google Closure Compiler](https://developers.google.com/closure/compiler/)
 * [UglifyJS](https://github.com/mishoo/UglifyJS2)

Uglify wins:

 * on-par with Google Closure rgd. results, but ..
 * written in JS, runs on Node (no need for Java)
 * fast

## Unit Tests

Of course there is [Jasmine](http://pivotal.github.io/jasmine/), [QUnit](http://qunitjs.com/) and [Mocha](http://visionmedia.github.io/mocha/). And there is a new kid on the block: [BusterJS](http://docs.busterjs.org/en/latest/).

### Promises

But we need be able to test cases that involve WAMP RPCs and PubSub events. Hence, see [here](http://stackoverflow.com/questions/18406594/js-test-framework-that-works-with-deferreds-promises).

BusterJS natively [supports](http://docs.busterjs.org/en/latest/modules/buster-test/test-case/#id1) testing functions returning promises.

### Headless

We want to automate testing. Hence we need to run tests in a headless browser environment. This is [supported](http://blog.knuthaugen.no/2012/09/headless-tests-with-buster-and-phantom/) by BusterJS via [PhantomJS](http://phantomjs.org/).

### Node

Probably we want to test JS in non-browser environments like Node or PostgreSQL. BusterJS was built with non-browser environments in mind.
