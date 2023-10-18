const { src, dest, parallel, series, watch } = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const autoprefixer = require('gulp-autoprefixer');
const cleancss = require('gulp-clean-css');
const del = import('del');
const browserify = require('browserify');
const glob = require('glob');
const path = require('path');

function styles() {
    return src('fastbarterApp/static/fastbarterApp/scss/*.scss')
        .pipe(sass())
        .pipe(autoprefixer({ overrideBrowserslist: ['last 10 versions'], grid: true }))
        .pipe(cleancss( { level: { 1: { specialComments: 0 } } } ))
        .pipe(dest('fastbarterApp/static/fastbarterApp/css/'))
}

exports.styles = styles;

function watchFiles() {
    watch("fastbarterApp/static/fastbarterApp/scss/**/*", styles);
}

exports.watch = watchFiles;

exports.build = styles;
