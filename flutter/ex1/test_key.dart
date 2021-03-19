import 'package:pinenacl/ed25519.dart';
import 'dart:io';

void main() {
    const hex = HexCoder.instance;

    final cskey_hex = Platform.environment['CSKEY'];
    print(cskey_hex.length);

    final signingKey = SigningKey(seed: hex.decode(cskey_hex));

    print(signingKey.publicKey.encode(HexCoder.instance));
}
