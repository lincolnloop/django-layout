// Plugins are resolved via require.resolve so prettier finds them in
// pre-commit's isolated node env (which sets NODE_PATH). A plain plugin-name
// array fails under pre-commit because prettier v3 loads plugins with ESM
// import(), which ignores NODE_PATH and only walks node_modules from cwd.
module.exports = {
  plugins: [
    require.resolve("prettier-plugin-jinja-template"),
    require.resolve("prettier-plugin-tailwindcss"),
  ],
  printWidth: 88,
  semi: true,
  singleAttributePerLine: true,
  singleQuote: false,
  tabWidth: 2,
  tailwindStylesheet: "ui/main.css",
  trailingComma: "all",
  overrides: [
    {
      files: ["*.html"],
      options: { parser: "jinja-template" },
    },
    {
      files: ["*.md"],
      options: { proseWrap: "always" },
    },
  ],
};
