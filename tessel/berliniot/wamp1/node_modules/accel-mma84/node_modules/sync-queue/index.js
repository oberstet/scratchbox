function queue() {

  // Create an empty array of commands
  var queue = [];
  // We're inactive to begin with
  queue.active = false;
  // Method for adding command chain to the queue
  queue.place = function (command) { 
    // Push the command onto the command array
    queue.push(command);
    // If we're currently inactive, start processing
    if (!queue.active) queue.next();
  };
  // Method for calling the next command chain in the array
  queue.next = function () {
    // If this is the end of the queue
    if (!queue.length) {
      // We're no longer active
      queue.active = false;
      // Stop execution
      return;
    } 
    // Grab the next command
    var command = queue.shift();
    // We're active
    queue.active = true;
    // Call the command
    command();
  };

  return queue;
}

module.exports = queue;