# GeoAce Frontend

This is the react frontend for konfetti. This project is strongly inspired by
[bulletproof-react](https://github.com/alan2207/bulletproof-react) and tries to replicate most parts of the project
structure, style guides and design patterns.

Important Frameworks used in this application:

-   [tanstack/react-query](https://tanstack.com/query/v4/docs/vue/overview) which provides hooks for fetching, caching
    and updating asynchronous data in Vue
-   [zustand](https://github.com/pmndrs/zustand) for complex stores
-   [jotai](https://jotai.org/) for simple global state
-   [MUI](https://mui.com/material-ui/) as the design system

## Project setup

```
pnpm install
```

### Automatically Format Code on File Save

By using Prettier you don’t have to worry about adding or removing space or moving code to the second line if it does
not fit on one line. Prettier does that job for you. It can be configured accordingly in most IDEs.

## 🗄️ Project Structure

Most of the code lives in the `src` folder and looks like this:

```sh
src
|
+-- api               # functions used for fetching (react-query)
|
+-- assets            # assets folder can contain all the static files such as images, fonts, etc.
|
+-- components        # shared components used across the entire application
|
+-- config            # shared global configs
|
+-- features          # feature based modules
|
+-- hooks             # shared hooks used across the entire application
|
+-- store             # shared stores used across the entire application
|
+-- pages             # views that will be accessible via routing
|
+-- utils             # shared utility functions
```

In order to scale the application in the easiest and most maintainable way, keep most of the code inside the `features`
folder, which should contain different feature-based things. Every `feature` folder should contain domain specific code
for a given feature. This will allow you to keep functionalities scoped to a feature and not mix its declarations with
shared things. This is much easier to maintain than a flat folder structure with many files.

A feature could have the following structure:

```sh
src/features/AwesomeFeature
|
+-- assets      # assets folder can contain all the static files for a specific feature
|
+-- components  # components scoped to a specific feature
|
+-- hooks       # hooks scoped to a specific feature
|
+-- store       # stores scoped to a specific feature
|
+-- utils       # utility functions for a specific feature
|
+-- index.js    # entry point for the feature, it should serve as the public API of the given feature and exports everything that should be used outside the feature
```

A feature folder could also contain other features (if used only within the parent feature) or be kept separated, it's a
matter of preference.

Everything from a feature should be exported from the `index.js` file which behaves as the public API of the feature.
You should import stuff from other features only by using:

`import {AwesomeComponent} from "/features/AwesomeFeature"`

and not

`import {AwesomeComponent} from "/features/AwesomeFeature/components/AwesomeComponent`

## 👁️ Style Guide

When you work with large projects, it's important that you remain consistent throughout the codebase and follow the best
practices. To guarantee the quality of your codebase, you need to analyze different levels of the applications code.

## Clean Code

This is the most abstract level of code standardization. It's related to the implementations independent of the
programming language. It will help the readability of your code.

[Clean Code Javascript](https://github.com/ryanmcdermott/clean-code-javascript)

### Naming

One of the most important points of the Clean Code is how you name your functions, variables, components, etc. Use this
amazing guide to understand how to write better variable names.

[Naming Cheatsheet](https://github.com/kettanaito/naming-cheatsheet)
