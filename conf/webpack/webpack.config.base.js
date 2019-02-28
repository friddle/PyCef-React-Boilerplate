/**
 * Base webpack config used across other specific configs
 */
import path from 'path';
import webpack from 'webpack';
import CopyWebpackPlugin from 'copy-webpack-plugin';
import { dependencies as externals } from '../../package.json';

export default {
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: {
            loader: 'babel-loader',
            options: {
                cacheDirectory: true,
            }
        }
      }
    ]
  },

    output: {
        path: path.join(__dirname, '../../', 'dist'),
    },

    /**
     * Determine the array of extensions that should be used to resolve modules.
     */
    resolve: {
        extensions: ['.js', '.jsx', '.json'],
        modules: [
            path.join(__dirname,'../../node_modules')
        ]
    },

    plugins: [
        new webpack.EnvironmentPlugin({
            NODE_ENV: 'production'
        }),

        new webpack.NamedModulesPlugin(),

        new CopyWebpackPlugin([
                { from: 'web/template/app.html', to:'./'}
            ]
        ),
    ]
};