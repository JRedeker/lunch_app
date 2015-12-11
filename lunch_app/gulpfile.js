var gulp = require('gulp');
var bower = require('gulp-bower');
// Include plugins
var concat = require('gulp-concat');
gulp.task('default', function() {
    // place code for your default task here
});
// Concatenate JS Files
gulp.task('scripts', function() {
    return gulp.src('src/js/*.js')
        .pipe(concat('main.js'))
        .pipe(gulp.dest('build/js'));
});
gulp.task('bower', function() {
    return bower('./static/js/bower_components')
        .pipe(gulp.dest('lib/'))
});