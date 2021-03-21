import 'package:connectanum/connectanum.dart';
import 'package:connectanum/src/authentication/cryptosign_authentication.dart';
// import 'package:connectanum/json.dart';
import 'package:connectanum/msgpack.dart';
import 'package:pedantic/pedantic.dart';
import 'package:convert/convert.dart';
import 'package:uuid/uuid.dart';
import 'package:uuid/uuid_util.dart';
import 'dart:io';

void main() async {
  // WAMP-Cryptosign private key (seed)
  final cskey_hex = Platform.environment['CSKEY'];

  // Ethereum private key (seed)
  final ethkey_hex = Platform.environment['ETHKEY'];

  final client1 = Client(
      realm: 'xbrnetwork',
      // realm: null,
      authenticationMethods: [
        CryptosignAuthentication.fromHex(cskey_hex)
      ],
      transport: WebSocketTransport(
        'ws://thingcloud-box-aws.sthngs.crossbario.com:8090/ws',
        // 'ws://thingcloud-box-aws.sthngs.crossbario.com:8080/ws',
        Serializer(),
        // WebSocketSerialization.SERIALIZATION_JSON,
        WebSocketSerialization.SERIALIZATION_MSGPACK,
      ));

  Session session1;

  try {
    session1 = await client1
        .connect(
            options: ClientConnectOptions(
                reconnectCount: 2,
                reconnectTime: Duration(milliseconds: 200)
                ))
        .first;

    print('authentication successful, session joined!');
    print('realm="${session1.realm}", session=${session1.id}, authmethod="${session1.authMethod}", authid="${session1.authId}", authrole="${session1.authRole}"');

    // 2) How to load Eth private key and compute public address?
    final ethkey_adr = hex.decode('e3E25EA345381FA5cD86715c78D64D8804D7DcF5');
    print('ethkey_adr length: ${ethkey_adr.length}');

    // This works, but I get sick from the syntax .. callback nesting hell.
    session1.call('xbr.network.is_member', arguments: [ethkey_adr]).listen(
      (result) {
        final bool is_member = result.arguments[0];
        if (is_member) {
          print('Address 0x${hex.encode(ethkey_adr)} already is a member in the network:');
          session1.call('xbr.network.get_member_by_wallet', arguments: [ethkey_adr]).listen(
            (result) {
              print('\n${result.arguments[0]}\n');
              // {oid: [147, 83, 131, 8, 138, 67, 67, 197, 164, 17, 174, 59, 75, 221, 91, 215],
              //  address: [227, 226, 94, 163, 69, 56, 31, 165, 205, 134, 113, 92, 120, 214, 77, 136, 4, 215, 220, 245],
              //  level: 1, profile: QmUEM5UuSUMeET2Zo8YQtDMK74Fr2SJGEyTokSYzT3uD94,
              //  eula: QmRgTwgj9b4j2DMZ9iGWkkFGY4gT6VBwYEE8KAfueE3S8p,
              //  balance: {
              //     xbr: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              //     eth: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
              //  email: tobias.oberstein@gmail.com,
              //  username: oberstet,
              //  created: 1614827037973698512,
              //  markets: 0,
              //  catalogs: 0,
              // domains: 0}

              // cast the generic Dart object into a dynamic map. awesome. whatever. this is required:
              final Map<dynamic, dynamic> m = result.arguments[0];

              // cast the items we care about
              final String oid = Uuid.unparse(m['oid']);
              final String address = hex.encode(m['address']);
              final int level = m['level'];
              final String profile = m['profile'];
              final String eula = m['eula'];
              final String email = m['email'];
              final String username = m['username'];

              // not yet available in Dart: https://github.com/dart-lang/sdk/issues/32803
              // we want to cast a uint256|bigendian into a BigInt
              // final BigInt eth = BigInt.fromBytes(m['balance']['eth']);
              final BigInt eth = BigInt.from(0);

              // this is also wrong in multiple ways: the Dart MsgPack serializer does unserialized the
              // value as Double, but it is a big integer. Further, the Dart DateTime class can't cope with
              // nanoseconds, so the timestamp can be wrong +/-1ms
              final DateTime created = DateTime.fromMicrosecondsSinceEpoch((m['created'] / 1000).toInt(), isUtc: true);

              print('oid=${oid}, created=${created}, address=${address}, level=${level}, profile=${profile}, eula=${eula}, email=${email}, username=${username}, eth=${eth}');
            },
            onError: (e) {
              var error = e as Error; // type cast necessary
              print(error.error);
            });
        } else {
          print('Address 0x${hex.encode(ethkey_adr)} is NOT yet a member in the network!');
        }
      },
      onError: (e) {
        var error = e as Error; // type cast necessary
        print(error.error);
      });

    // This does not work .. why?
    final result = await session1.call('xbr.network.is_member', arguments: [ethkey_adr]).first;
    print('RPC result: ${result}');

    final bool is_member = result.arguments[0];
    if (is_member) {
      print('Address ${ethkey_adr} already is a member in the network:');
      // final member_data = await session1.call('xbr.network.get_member_by_wallet', ethkey_adr);
    } else {
      print('Address ${ethkey_adr} is NOT yet a member in the network!');
    }

    // How to leave session and disconnect?
    // session1.close();

  } on Abort catch (abort) {
    print(abort.message.message);
  }
  catch (e) {
    print(e);
  }
}
