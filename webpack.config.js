// https://github.com/baileyherbert/svelte-webpack-starter

const path = require("path");
const SveltePreprocess = require("svelte-preprocess");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

const SvelteDevConfig = {
    compilerOptions: {
        dev: true
    },
    emitCss: false,
    hotReload: true,
    hotOptions: {
        noPreserveState: false,
        optimistic: true,
    },
    preprocess: SveltePreprocess({
        scss: false,
        sass: false,
    })
}

const SvelteProdConfig = {
    compilerOptions: {
        dev: false
    },
    emitCss: false,
    hotReload: false,
    hotOptions: {
        preserveLocalState: false,
        noPreserveStateKey: "@!hmr",
        noReload: false,
        optimistic: false,
        acceptAccessors: true,
        acceptNamedExports: true,
    },
    preprocess: SveltePreprocess({
        scss: false,
        sass: false,
    })
}


module.exports = {
    context: __dirname,
    entry: {
        style: "./inventory_fe/js/style.js",
        inventoryList: "./inventory_fe/pages/inventoryList/index.ts"
    },
    resolve: {
        alias: {
            svelte: path.resolve('node_modules', 'svelte/src/runtime'),
        },
        extensions: [".mjs", ".js", ".ts", ".svelte"],
        mainFields: ["svelte", "browser", "module", "main"],
        conditionNames: ["svelte", "browser"]
    },
    output: {
        path: path.resolve("./static/"),
        filename: "[name].js",
        chunkFilename: "chunk.[id].js",
    },
    plugins: [
        new MiniCssExtractPlugin(),
    ],
    module: {
        rules: [
            {
                test: /\.(sa|sc|c)ss$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    "css-loader",
                    "postcss-loader",
                    "sass-loader",
                ],
                exclude: /node_modules/,
            },
            {
                test: /\.svelte$/,
                use: {
                    loader: "svelte-loader",
                    options: process.env.NODE_ENV === "production" ? SvelteProdConfig : SvelteDevConfig
                }
            },
            {
                test: /\.tsx?$/,
                use: "ts-loader",
                exclude: /node_modules/,
            },
            {
                test: /node_modules\/svelte\/.*\.mjs$/,
                resolve: {
                    fullySpecified: false
                }
            },
        ]
    }
}
