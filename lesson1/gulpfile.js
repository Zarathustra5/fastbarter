const { src, dest, parallel, series, watch } = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const autoprefixer = require('gulp-autoprefixer');
const cleancss = require('gulp-clean-css');
const del = import('del');
const browserify = require('browserify');
const glob = require('glob');
const path = require('path');

function styles() {
    return src('lesson1App/static/lesson1App/scss/*.scss')
        .pipe(sass())
        .pipe(autoprefixer({ overrideBrowserslist: ['last 10 versions'], grid: true }))
        .pipe(cleancss( { level: { 1: { specialComments: 0 } } } ))
        .pipe(dest('lesson1App/static/lesson1App/css/'))
}

exports.styles = styles;

function watchFiles() {
    watch("lesson1App/static/lesson1App/scss/**/*", styles);
}

exports.watch = watchFiles;

exports.build = styles;
