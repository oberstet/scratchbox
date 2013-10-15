###
https://gist.github.com/idanz/6411301
inspired from  http://www.knockmeout.net/2011/04/pausing-notifications-in-knockoutjs.html , with the following changes
1. Pause never causes trigger or computation
2. Resume only causes trigger if the computed dependencies were triggered while it was paused
3. Pause and Resume can be nested without any additional triggers or computation
###
ko.pauseableComputed = (evaluatorFunction, evaluatorTarget) ->
    isPaused = ko.observable(false)
    pauseCounter = ko.observable(0)
    # Using this method ensures that when the counter goes from 1 to 2, the isPaused observable does not trigger again
    ko.computed(=> isPaused(pauseCounter() > 0))

    notify = []
    #the computed observable that we will return
    result = ko.computed(->
        # Check if we are in paused mode without depending on the observable
        # so the actual pausing will not trigger the event
        if isPaused.peek()
            # In case we are paused, we need to depend on the observable so we recalculate when resumed
            isPaused()
            result.peek()
        else
            evaluatorFunction.call(evaluatorTarget)
    )

    result.pause = ->
        if not isPaused() # First pause call
            # Remove the notification method to ensure we don't fire while paused
            notify.push(result.notifySubscribers)
            result.notifySubscribers = ->
        pauseCounter(pauseCounter() + 1);

    result.resume = ->
        # Return the trigger method to the computed, so if changes occurred while we were paused, they will be notified
        result.notifySubscribers = notify[0]
        # The resume will only trigger an update iff any of the original dependencies have been triggerred while we were paused
        pauseCounter(pauseCounter() - 1)

    return result
