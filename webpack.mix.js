// webpack.mix.js

const { sourceMaps } = require('laravel-mix');
const mix = require('laravel-mix');


// let staticPath = "static/build";
// let resourcesPath = "resources";

// mix.setResourceRoot("build"); // setResroucesRoots add prefix to url() in scss on example: from /images/close.svg to /static/images/close.svg
// mix.setPublicPath("static"); // Path where mix-manifest.json is created

// if you don't need browser-sync feature you can remove this lines
// if (process.argv.includes("--browser-sync")) {
//     mix.browserSync("localhost:8000");
// }


mix.webpackConfig({
  devtool: false
})
mix.browserSync({                                     // 6. Browsersync
  files: 'static/**/*',                            // (3.Uglify と 5.Watch は記述不要)
  server: 'staic',
  proxy: false
});



// Now you can use full mix api
// Refer the file that was created in Step 2 to be compile
mix.sourceMaps()
mix.js(`resources/js/main.js`, `build/main.js`)
  .vue({ varsion: 2 })
mix.sass(`resources/sass/app.scss`, `build/app.css`);
mix.setPublicPath("static")



/*"name": "vuedjango",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",*/



