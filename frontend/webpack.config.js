const HtmlWebpackPlugin = require('html-webpack-plugin')
const path = require('path');
const webpack  = require('webpack');

module.exports = (env) => {
    return {
        target: 'web',
        mode: env.mode,
        entry: './src/index.jsx',
        externals: 'fs',
        output: {
            path: path.resolve(__dirname, 'build'),
            filename: '[name].bundle.js',
        },
        module: {
            rules: [
                {
                    test: /\.(js|jsx)$/,
                    exclude: /node_modules/,
                    loader: "babel-loader",
                    options: {
                        presets:[ "@babel/preset-react"]
                    }
                },
                {
                    test: /\.css$/i,
                    use: ["style-loader", "css-loader"],
                }
            ]
        },
        plugins: [
            new HtmlWebpackPlugin({
                template: path.resolve(__dirname, 'public/index.html'),
                filename: 'index.html'
            }),
            new webpack.optimize.LimitChunkCountPlugin({
                maxChunks: 1,
            })
        ]
    }
}