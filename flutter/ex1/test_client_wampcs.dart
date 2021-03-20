import 'package:connectanum/connectanum.dart';
import 'package:connectanum/src/authentication/cryptosign_authentication.dart';
import 'package:connectanum/json.dart';
import 'package:pedantic/pedantic.dart';
import 'dart:io';

void main() async {
  // WAMP-Cryptosign private key (seed)
  final cskey_hex = Platform.environment['CSKEY'];

  // Ethereum private key (seed)
  final ethkey_hex = Platform.environment['ETHKEY'];

  final client1 = Client(
      // realm: 'xbrnetwork',
      realm: null,
      authenticationMethods: [
        CryptosignAuthentication.fromHex(cskey_hex)
      ],
      transport: WebSocketTransport(
        // 'ws://thingcloud-box-aws.sthngs.crossbario.com:8090/ws',
        'ws://thingcloud-box-aws.sthngs.crossbario.com:8080/ws',
        Serializer(),
        WebSocketSerialization.SERIALIZATION_JSON,
      ));

  Session session1;

  try {
    session1 = await client1
        .connect(
            options: ClientConnectOptions(
                reconnectCount: 10,
                reconnectTime: Duration(milliseconds: 200)
                ))
        .first;

    print('authentication successful, session joined!');
    print('realm="${session1.realm}", session=${session1.id}, authmethod="${session1.authMethod}", authid="${session1.authId}", authrole="${session1.authRole}"');

    // Accept(realm=<member-93538308-8a43-43c5-a411-ae3b4bdd5bd7>, authid=<member-93538308-8a43-43c5-a411-ae3b4bdd5bd7>, authrole=<anonymous>, authmethod=cryptosign, authprovider=function, authextra={'member_oid': '93538308-8a43-43c5-a411-ae3b4bdd5bd7', 'credential_oid': '8c9b887c-95a0-4b2d-812e-7ee5bc9f91ce'})

    // How to leave session and disconnect?
    session1.close();

    // // 2) How to load Eth private key and compute public address?
    // final String ethkey_adr = '0xe3E25EA345381FA5cD86715c78D64D8804D7DcF5';

    // // 3) How to fix "Error: Too many positional arguments: 1 allowed, but 2 found."?
    // final bool is_member = await session1.call('xbr.network.is_member', ethkey_adr);

    // if (is_member) {
    //   print('Address $ethkey_adr already is a member in the network:');
    //   final member_data = await session1.call('xbr.network.get_member_by_wallet', ethkey_adr);
    //   print(member_data);
    // } else {
    //   print('Address $ethkey_adr is NOT yet a member in the network!');
    // }

  } on Abort catch (abort) {
    print(abort.message.message);
  }
}
