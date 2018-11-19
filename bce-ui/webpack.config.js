const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const path = require('path');

module.exports = {
  entry: './src/main.ts',
  module: {
    rules: [
      {
        test: /\.ts$/,
        use: ['ts-loader', 'angular2-template-loader'],
        exclude: /node_modules/
      },
      {
        test: /\.(html|css)$/,
        loader: 'raw-loader'
      },
      {
        test: /\.scss$/,
        loaders: [ 'to-string-loader', 'style-loader', 'css-loader', 'sass-loader']
        //include: [helpers.root( 'src', 'styles' )]
      }
    ]
  },
  resolve: {
    extensions: ['.ts', '.js', '.css', '.scss'],
    //alias: {
    //  '@': path.resolve(__dirname, 'src/app/'),
    //}
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html',
      filename: 'index.html',
      inject: 'body'
    }),
    new webpack.DefinePlugin({
      // global app config object
      config: JSON.stringify({
        apiUrl: 'http://localhost:8000'
      })
    })
  ],
  optimization: {
    splitChunks: {
      chunks: 'all',
    },
    runtimeChunk: true
  },
  devServer: {
    historyApiFallback: true
  }
};
