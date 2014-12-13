/* test rig */ var t = 1, tmax = 5
function ok (a, d) { console.log(a ? 'ok ' + (t++) + ' -' : 'not ok ' + (t++) + ' -', d); }
console.log(t + '..' + tmax);

/* script */

var tessel = require('tessel');
var accel = require('../').use(tessel.port[process.argv[2] || 'A']);

accel.on('sample', function (xyz) {
  ok(Array.isArray(xyz), 'accelerometer data is array');
  ok(xyz.length == 3, 'three samples');
  ok(typeof xyz[0] == 'number', 'idx 0 is number');
  ok(typeof xyz[1] == 'number', 'idx 1 is number');
  ok(typeof xyz[2] == 'number', 'idx 2 is number');
  process.exit(0);
});
