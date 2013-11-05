import sys, time, struct, random, os


def fake_test_masker(Masker, params):

   msg_cnt, frame_cnt, chop_cnt, chop_size = params
   total_length = frame_cnt * chop_cnt * chop_size

   print "Using XOR masker", str(M)
   print "WebSocket Message (%d frames, %d chops, %d chop size, %d total length)" % (frame_cnt, chop_cnt, chop_size, total_length)
   print "Processing %d messages (%d total payload).." % (msg_cnt, msg_cnt * total_length)

   ## synthesize a WebSocket message, which consists of
   ## a number of WebSocket frames, each having a different mask,
   ## and which we receive in chops (since TCP is stream-based)
   ##
   frames = []
   for i in xrange(frame_cnt):
      mask = struct.pack("!I", random.getrandbits(32))
      chunks = []
      for j in xrange(chop_cnt):
         payload = os.urandom(chop_size)
         chunks.append(payload)
      frames.append((mask, chunks))


   ## and now simulate unmasking of the msg_cnt messages
   ##
   t0 = time.time()
   for k in xrange(msg_cnt):

      unmaskedFramePayloads = []

      ## Since the mask is applied sliding over the data received
      ## in chops for a _frame_, the masker must keep state.
      ##
      for mask, chunks in frames:
         masker = Masker(mask)
         unmaskedChunks = []
         for chunk in chunks:
            unmaskedChunks.append(masker.process(chunk))

      unmaskedMessagePayload = ''.join(unmaskedFramePayloads)

   t1 = time.time()
   print "Runtime", t1 - t0
   print


if __name__ == '__main__':
   MASKERS = []

   if 'PyPy' in sys.version:
      from xormasker import XorMaskerSimple as XorMaskerSimplePy
      MASKERS.append(XorMaskerSimplePy)

      from xormasker import XorMaskerShifted1 as XorMaskerShifted1Py
      MASKERS.append(XorMaskerShifted1Py)
   else:
      print
      print "!!! Skipping pure Python maskers when running CPython [way too slow]"
      print

   try:
      from wsaccel.xormask import XorMaskerSimple as XorMaskerSimpleWsAccel
      MASKERS.append(XorMaskerSimpleWsAccel)
   except:
      print
      print "!!! wsaccel not installed"
      print

   ## Of course the specific parameters chosen below for synthesizing
   ## a messages will affect the performance. In practice, this will
   ## vary depending on actual traffic on the WebSocket connection.
   ##
   ## (msg_cnt, frame_cnt, chop_cnt, chop_size)
   ##
   ## msg_cnt:   number of WebSocket message processed in run
   ## frame_cnt: number of WebSocket frames the WebSocket message consists of
   ## chop_cnt:  number of chops in which we receive a single frame from TCP
   ## chop_size: octets we receive in each chop
   ##
   params_sets = [(10, 1, 1, 100000000),
                  (100, 100, 100, 1000),
                  (100, 10, 10000, 100),
                  (10000000, 1, 1, 100)]

   for params in params_sets:
      for M in MASKERS:
         fake_test_masker(M, params)
