// automatically generated by the FlatBuffers compiler, do not modify



use crate::types_generated::*;
use crate::roles_generated::*;
use crate::auth_generated::*;
use crate::auth_generated::wamp::proto::AuthMethod;
use core::mem;
use core::cmp::Ordering;

extern crate flatbuffers;
use self::flatbuffers::{EndianScalar, Follow};

#[allow(unused_imports, dead_code)]
pub mod wamp {

  use crate::types_generated::*;
  use crate::types_generated::wamp::Map;
  use crate::types_generated::wamp::proto::MessageType;
  use crate::types_generated::wamp::proto::Payload;
  use crate::types_generated::wamp::proto::Serializer;
  use crate::roles_generated::*;
  use crate::auth_generated::*;
  use crate::auth_generated::wamp::proto::AuthMethod;
  use core::mem;
  use core::cmp::Ordering;

  extern crate flatbuffers;
  use self::flatbuffers::{EndianScalar, Follow};
#[allow(unused_imports, dead_code)]
pub mod proto {

  use crate::types_generated::*;
  use crate::types_generated::wamp::Map;
  use crate::types_generated::wamp::proto::MessageType;
  use crate::types_generated::wamp::proto::Payload;
  use crate::types_generated::wamp::proto::Serializer;
  use crate::roles_generated::*;
  use crate::roles_generated::wamp::proto::ClientRoles;
  use crate::roles_generated::wamp::proto::RouterRoles;
  use crate::auth_generated::*;
  use crate::auth_generated::wamp::proto::AuthMethod;
  use core::mem;
  use core::cmp::Ordering;

  extern crate flatbuffers;
  use self::flatbuffers::{EndianScalar, Follow};

pub enum HelloOffset {}
#[derive(Copy, Clone, PartialEq)]

pub struct Hello<'a> {
  pub _tab: flatbuffers::Table<'a>,
}

impl<'a> flatbuffers::Follow<'a> for Hello<'a> {
  type Inner = Hello<'a>;
  #[inline]
  fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
    Self { _tab: flatbuffers::Table { buf, loc } }
  }
}

impl<'a> Hello<'a> {
  pub const VT_ROLES: flatbuffers::VOffsetT = 4;
  pub const VT_REALM: flatbuffers::VOffsetT = 6;
  pub const VT_AUTHMETHODS: flatbuffers::VOffsetT = 8;
  pub const VT_AUTHID: flatbuffers::VOffsetT = 10;
  pub const VT_AUTHROLE: flatbuffers::VOffsetT = 12;
  pub const VT_AUTHEXTRA: flatbuffers::VOffsetT = 14;
  pub const VT_RESUMABLE: flatbuffers::VOffsetT = 16;
  pub const VT_RESUME_SESSION: flatbuffers::VOffsetT = 18;
  pub const VT_RESUME_TOKEN: flatbuffers::VOffsetT = 20;

  #[inline]
  pub fn init_from_table(table: flatbuffers::Table<'a>) -> Self {
    Hello { _tab: table }
  }
  #[allow(unused_mut)]
  pub fn create<'bldr: 'args, 'args: 'mut_bldr, 'mut_bldr>(
    _fbb: &'mut_bldr mut flatbuffers::FlatBufferBuilder<'bldr>,
    args: &'args HelloArgs<'args>
  ) -> flatbuffers::WIPOffset<Hello<'bldr>> {
    let mut builder = HelloBuilder::new(_fbb);
    builder.add_resume_session(args.resume_session);
    if let Some(x) = args.resume_token { builder.add_resume_token(x); }
    if let Some(x) = args.authextra { builder.add_authextra(x); }
    if let Some(x) = args.authrole { builder.add_authrole(x); }
    if let Some(x) = args.authid { builder.add_authid(x); }
    if let Some(x) = args.authmethods { builder.add_authmethods(x); }
    if let Some(x) = args.realm { builder.add_realm(x); }
    if let Some(x) = args.roles { builder.add_roles(x); }
    builder.add_resumable(args.resumable);
    builder.finish()
  }


  #[inline]
  pub fn roles(&self) -> ClientRoles<'a> {
    self._tab.get::<flatbuffers::ForwardsUOffset<ClientRoles>>(Hello::VT_ROLES, None).unwrap()
  }
  #[inline]
  pub fn realm(&self) -> Option<&'a str> {
    self._tab.get::<flatbuffers::ForwardsUOffset<&str>>(Hello::VT_REALM, None)
  }
  #[inline]
  pub fn authmethods(&self) -> Option<flatbuffers::Vector<'a, AuthMethod>> {
    self._tab.get::<flatbuffers::ForwardsUOffset<flatbuffers::Vector<'a, AuthMethod>>>(Hello::VT_AUTHMETHODS, None)
  }
  #[inline]
  pub fn authid(&self) -> Option<&'a str> {
    self._tab.get::<flatbuffers::ForwardsUOffset<&str>>(Hello::VT_AUTHID, None)
  }
  #[inline]
  pub fn authrole(&self) -> Option<&'a str> {
    self._tab.get::<flatbuffers::ForwardsUOffset<&str>>(Hello::VT_AUTHROLE, None)
  }
  #[inline]
  pub fn authextra(&self) -> Option<super::Map<'a>> {
    self._tab.get::<flatbuffers::ForwardsUOffset<super::Map>>(Hello::VT_AUTHEXTRA, None)
  }
  #[inline]
  pub fn resumable(&self) -> bool {
    self._tab.get::<bool>(Hello::VT_RESUMABLE, Some(false)).unwrap()
  }
  #[inline]
  pub fn resume_session(&self) -> u64 {
    self._tab.get::<u64>(Hello::VT_RESUME_SESSION, Some(0)).unwrap()
  }
  #[inline]
  pub fn resume_token(&self) -> Option<&'a str> {
    self._tab.get::<flatbuffers::ForwardsUOffset<&str>>(Hello::VT_RESUME_TOKEN, None)
  }
}

impl flatbuffers::Verifiable for Hello<'_> {
  #[inline]
  fn run_verifier(
    v: &mut flatbuffers::Verifier, pos: usize
  ) -> Result<(), flatbuffers::InvalidFlatbuffer> {
    use self::flatbuffers::Verifiable;
    v.visit_table(pos)?
     .visit_field::<flatbuffers::ForwardsUOffset<ClientRoles>>("roles", Self::VT_ROLES, true)?
     .visit_field::<flatbuffers::ForwardsUOffset<&str>>("realm", Self::VT_REALM, false)?
     .visit_field::<flatbuffers::ForwardsUOffset<flatbuffers::Vector<'_, AuthMethod>>>("authmethods", Self::VT_AUTHMETHODS, false)?
     .visit_field::<flatbuffers::ForwardsUOffset<&str>>("authid", Self::VT_AUTHID, false)?
     .visit_field::<flatbuffers::ForwardsUOffset<&str>>("authrole", Self::VT_AUTHROLE, false)?
     .visit_field::<flatbuffers::ForwardsUOffset<super::Map>>("authextra", Self::VT_AUTHEXTRA, false)?
     .visit_field::<bool>("resumable", Self::VT_RESUMABLE, false)?
     .visit_field::<u64>("resume_session", Self::VT_RESUME_SESSION, false)?
     .visit_field::<flatbuffers::ForwardsUOffset<&str>>("resume_token", Self::VT_RESUME_TOKEN, false)?
     .finish();
    Ok(())
  }
}
pub struct HelloArgs<'a> {
    pub roles: Option<flatbuffers::WIPOffset<ClientRoles<'a>>>,
    pub realm: Option<flatbuffers::WIPOffset<&'a str>>,
    pub authmethods: Option<flatbuffers::WIPOffset<flatbuffers::Vector<'a, AuthMethod>>>,
    pub authid: Option<flatbuffers::WIPOffset<&'a str>>,
    pub authrole: Option<flatbuffers::WIPOffset<&'a str>>,
    pub authextra: Option<flatbuffers::WIPOffset<super::Map<'a>>>,
    pub resumable: bool,
    pub resume_session: u64,
    pub resume_token: Option<flatbuffers::WIPOffset<&'a str>>,
}
impl<'a> Default for HelloArgs<'a> {
  #[inline]
  fn default() -> Self {
    HelloArgs {
      roles: None, // required field
      realm: None,
      authmethods: None,
      authid: None,
      authrole: None,
      authextra: None,
      resumable: false,
      resume_session: 0,
      resume_token: None,
    }
  }
}

pub struct HelloBuilder<'a: 'b, 'b> {
  fbb_: &'b mut flatbuffers::FlatBufferBuilder<'a>,
  start_: flatbuffers::WIPOffset<flatbuffers::TableUnfinishedWIPOffset>,
}
impl<'a: 'b, 'b> HelloBuilder<'a, 'b> {
  #[inline]
  pub fn add_roles(&mut self, roles: flatbuffers::WIPOffset<ClientRoles<'b >>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<ClientRoles>>(Hello::VT_ROLES, roles);
  }
  #[inline]
  pub fn add_realm(&mut self, realm: flatbuffers::WIPOffset<&'b  str>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<_>>(Hello::VT_REALM, realm);
  }
  #[inline]
  pub fn add_authmethods(&mut self, authmethods: flatbuffers::WIPOffset<flatbuffers::Vector<'b , AuthMethod>>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<_>>(Hello::VT_AUTHMETHODS, authmethods);
  }
  #[inline]
  pub fn add_authid(&mut self, authid: flatbuffers::WIPOffset<&'b  str>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<_>>(Hello::VT_AUTHID, authid);
  }
  #[inline]
  pub fn add_authrole(&mut self, authrole: flatbuffers::WIPOffset<&'b  str>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<_>>(Hello::VT_AUTHROLE, authrole);
  }
  #[inline]
  pub fn add_authextra(&mut self, authextra: flatbuffers::WIPOffset<super::Map<'b >>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<super::Map>>(Hello::VT_AUTHEXTRA, authextra);
  }
  #[inline]
  pub fn add_resumable(&mut self, resumable: bool) {
    self.fbb_.push_slot::<bool>(Hello::VT_RESUMABLE, resumable, false);
  }
  #[inline]
  pub fn add_resume_session(&mut self, resume_session: u64) {
    self.fbb_.push_slot::<u64>(Hello::VT_RESUME_SESSION, resume_session, 0);
  }
  #[inline]
  pub fn add_resume_token(&mut self, resume_token: flatbuffers::WIPOffset<&'b  str>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<_>>(Hello::VT_RESUME_TOKEN, resume_token);
  }
  #[inline]
  pub fn new(_fbb: &'b mut flatbuffers::FlatBufferBuilder<'a>) -> HelloBuilder<'a, 'b> {
    let start = _fbb.start_table();
    HelloBuilder {
      fbb_: _fbb,
      start_: start,
    }
  }
  #[inline]
  pub fn finish(self) -> flatbuffers::WIPOffset<Hello<'a>> {
    let o = self.fbb_.end_table(self.start_);
    self.fbb_.required(o, Hello::VT_ROLES,"roles");
    flatbuffers::WIPOffset::new(o.value())
  }
}

impl core::fmt::Debug for Hello<'_> {
  fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
    let mut ds = f.debug_struct("Hello");
      ds.field("roles", &self.roles());
      ds.field("realm", &self.realm());
      ds.field("authmethods", &self.authmethods());
      ds.field("authid", &self.authid());
      ds.field("authrole", &self.authrole());
      ds.field("authextra", &self.authextra());
      ds.field("resumable", &self.resumable());
      ds.field("resume_session", &self.resume_session());
      ds.field("resume_token", &self.resume_token());
      ds.finish()
  }
}
pub enum WelcomeOffset {}
#[derive(Copy, Clone, PartialEq)]

pub struct Welcome<'a> {
  pub _tab: flatbuffers::Table<'a>,
}

impl<'a> flatbuffers::Follow<'a> for Welcome<'a> {
  type Inner = Welcome<'a>;
  #[inline]
  fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
    Self { _tab: flatbuffers::Table { buf, loc } }
  }
}

impl<'a> Welcome<'a> {
  pub const VT_ROLES: flatbuffers::VOffsetT = 4;
  pub const VT_SESSION: flatbuffers::VOffsetT = 6;
  pub const VT_REALM: flatbuffers::VOffsetT = 8;
  pub const VT_AUTHID: flatbuffers::VOffsetT = 10;
  pub const VT_AUTHROLE: flatbuffers::VOffsetT = 12;
  pub const VT_AUTHMETHOD: flatbuffers::VOffsetT = 14;
  pub const VT_AUTHPROVIDER: flatbuffers::VOffsetT = 16;
  pub const VT_AUTHEXTRA: flatbuffers::VOffsetT = 18;
  pub const VT_RESUMED: flatbuffers::VOffsetT = 20;
  pub const VT_RESUMABLE: flatbuffers::VOffsetT = 22;
  pub const VT_RESUME_TOKEN: flatbuffers::VOffsetT = 24;

  #[inline]
  pub fn init_from_table(table: flatbuffers::Table<'a>) -> Self {
    Welcome { _tab: table }
  }
  #[allow(unused_mut)]
  pub fn create<'bldr: 'args, 'args: 'mut_bldr, 'mut_bldr>(
    _fbb: &'mut_bldr mut flatbuffers::FlatBufferBuilder<'bldr>,
    args: &'args WelcomeArgs<'args>
  ) -> flatbuffers::WIPOffset<Welcome<'bldr>> {
    let mut builder = WelcomeBuilder::new(_fbb);
    builder.add_session(args.session);
    if let Some(x) = args.resume_token { builder.add_resume_token(x); }
    if let Some(x) = args.authextra { builder.add_authextra(x); }
    if let Some(x) = args.authprovider { builder.add_authprovider(x); }
    if let Some(x) = args.authrole { builder.add_authrole(x); }
    if let Some(x) = args.authid { builder.add_authid(x); }
    if let Some(x) = args.realm { builder.add_realm(x); }
    if let Some(x) = args.roles { builder.add_roles(x); }
    builder.add_resumable(args.resumable);
    builder.add_resumed(args.resumed);
    builder.add_authmethod(args.authmethod);
    builder.finish()
  }


  #[inline]
  pub fn roles(&self) -> RouterRoles<'a> {
    self._tab.get::<flatbuffers::ForwardsUOffset<RouterRoles>>(Welcome::VT_ROLES, None).unwrap()
  }
  #[inline]
  pub fn session(&self) -> u64 {
    self._tab.get::<u64>(Welcome::VT_SESSION, Some(0)).unwrap()
  }
  #[inline]
  pub fn realm(&self) -> &'a str {
    self._tab.get::<flatbuffers::ForwardsUOffset<&str>>(Welcome::VT_REALM, None).unwrap()
  }
  #[inline]
  pub fn authid(&self) -> &'a str {
    self._tab.get::<flatbuffers::ForwardsUOffset<&str>>(Welcome::VT_AUTHID, None).unwrap()
  }
  #[inline]
  pub fn authrole(&self) -> &'a str {
    self._tab.get::<flatbuffers::ForwardsUOffset<&str>>(Welcome::VT_AUTHROLE, None).unwrap()
  }
  #[inline]
  pub fn authmethod(&self) -> AuthMethod {
    self._tab.get::<AuthMethod>(Welcome::VT_AUTHMETHOD, Some(AuthMethod::ANONYMOUS)).unwrap()
  }
  #[inline]
  pub fn authprovider(&self) -> Option<&'a str> {
    self._tab.get::<flatbuffers::ForwardsUOffset<&str>>(Welcome::VT_AUTHPROVIDER, None)
  }
  #[inline]
  pub fn authextra(&self) -> Option<super::Map<'a>> {
    self._tab.get::<flatbuffers::ForwardsUOffset<super::Map>>(Welcome::VT_AUTHEXTRA, None)
  }
  #[inline]
  pub fn resumed(&self) -> bool {
    self._tab.get::<bool>(Welcome::VT_RESUMED, Some(false)).unwrap()
  }
  #[inline]
  pub fn resumable(&self) -> bool {
    self._tab.get::<bool>(Welcome::VT_RESUMABLE, Some(false)).unwrap()
  }
  #[inline]
  pub fn resume_token(&self) -> Option<&'a str> {
    self._tab.get::<flatbuffers::ForwardsUOffset<&str>>(Welcome::VT_RESUME_TOKEN, None)
  }
}

impl flatbuffers::Verifiable for Welcome<'_> {
  #[inline]
  fn run_verifier(
    v: &mut flatbuffers::Verifier, pos: usize
  ) -> Result<(), flatbuffers::InvalidFlatbuffer> {
    use self::flatbuffers::Verifiable;
    v.visit_table(pos)?
     .visit_field::<flatbuffers::ForwardsUOffset<RouterRoles>>("roles", Self::VT_ROLES, true)?
     .visit_field::<u64>("session", Self::VT_SESSION, false)?
     .visit_field::<flatbuffers::ForwardsUOffset<&str>>("realm", Self::VT_REALM, true)?
     .visit_field::<flatbuffers::ForwardsUOffset<&str>>("authid", Self::VT_AUTHID, true)?
     .visit_field::<flatbuffers::ForwardsUOffset<&str>>("authrole", Self::VT_AUTHROLE, true)?
     .visit_field::<AuthMethod>("authmethod", Self::VT_AUTHMETHOD, false)?
     .visit_field::<flatbuffers::ForwardsUOffset<&str>>("authprovider", Self::VT_AUTHPROVIDER, false)?
     .visit_field::<flatbuffers::ForwardsUOffset<super::Map>>("authextra", Self::VT_AUTHEXTRA, false)?
     .visit_field::<bool>("resumed", Self::VT_RESUMED, false)?
     .visit_field::<bool>("resumable", Self::VT_RESUMABLE, false)?
     .visit_field::<flatbuffers::ForwardsUOffset<&str>>("resume_token", Self::VT_RESUME_TOKEN, false)?
     .finish();
    Ok(())
  }
}
pub struct WelcomeArgs<'a> {
    pub roles: Option<flatbuffers::WIPOffset<RouterRoles<'a>>>,
    pub session: u64,
    pub realm: Option<flatbuffers::WIPOffset<&'a str>>,
    pub authid: Option<flatbuffers::WIPOffset<&'a str>>,
    pub authrole: Option<flatbuffers::WIPOffset<&'a str>>,
    pub authmethod: AuthMethod,
    pub authprovider: Option<flatbuffers::WIPOffset<&'a str>>,
    pub authextra: Option<flatbuffers::WIPOffset<super::Map<'a>>>,
    pub resumed: bool,
    pub resumable: bool,
    pub resume_token: Option<flatbuffers::WIPOffset<&'a str>>,
}
impl<'a> Default for WelcomeArgs<'a> {
  #[inline]
  fn default() -> Self {
    WelcomeArgs {
      roles: None, // required field
      session: 0,
      realm: None, // required field
      authid: None, // required field
      authrole: None, // required field
      authmethod: AuthMethod::ANONYMOUS,
      authprovider: None,
      authextra: None,
      resumed: false,
      resumable: false,
      resume_token: None,
    }
  }
}

pub struct WelcomeBuilder<'a: 'b, 'b> {
  fbb_: &'b mut flatbuffers::FlatBufferBuilder<'a>,
  start_: flatbuffers::WIPOffset<flatbuffers::TableUnfinishedWIPOffset>,
}
impl<'a: 'b, 'b> WelcomeBuilder<'a, 'b> {
  #[inline]
  pub fn add_roles(&mut self, roles: flatbuffers::WIPOffset<RouterRoles<'b >>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<RouterRoles>>(Welcome::VT_ROLES, roles);
  }
  #[inline]
  pub fn add_session(&mut self, session: u64) {
    self.fbb_.push_slot::<u64>(Welcome::VT_SESSION, session, 0);
  }
  #[inline]
  pub fn add_realm(&mut self, realm: flatbuffers::WIPOffset<&'b  str>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<_>>(Welcome::VT_REALM, realm);
  }
  #[inline]
  pub fn add_authid(&mut self, authid: flatbuffers::WIPOffset<&'b  str>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<_>>(Welcome::VT_AUTHID, authid);
  }
  #[inline]
  pub fn add_authrole(&mut self, authrole: flatbuffers::WIPOffset<&'b  str>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<_>>(Welcome::VT_AUTHROLE, authrole);
  }
  #[inline]
  pub fn add_authmethod(&mut self, authmethod: AuthMethod) {
    self.fbb_.push_slot::<AuthMethod>(Welcome::VT_AUTHMETHOD, authmethod, AuthMethod::ANONYMOUS);
  }
  #[inline]
  pub fn add_authprovider(&mut self, authprovider: flatbuffers::WIPOffset<&'b  str>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<_>>(Welcome::VT_AUTHPROVIDER, authprovider);
  }
  #[inline]
  pub fn add_authextra(&mut self, authextra: flatbuffers::WIPOffset<super::Map<'b >>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<super::Map>>(Welcome::VT_AUTHEXTRA, authextra);
  }
  #[inline]
  pub fn add_resumed(&mut self, resumed: bool) {
    self.fbb_.push_slot::<bool>(Welcome::VT_RESUMED, resumed, false);
  }
  #[inline]
  pub fn add_resumable(&mut self, resumable: bool) {
    self.fbb_.push_slot::<bool>(Welcome::VT_RESUMABLE, resumable, false);
  }
  #[inline]
  pub fn add_resume_token(&mut self, resume_token: flatbuffers::WIPOffset<&'b  str>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<_>>(Welcome::VT_RESUME_TOKEN, resume_token);
  }
  #[inline]
  pub fn new(_fbb: &'b mut flatbuffers::FlatBufferBuilder<'a>) -> WelcomeBuilder<'a, 'b> {
    let start = _fbb.start_table();
    WelcomeBuilder {
      fbb_: _fbb,
      start_: start,
    }
  }
  #[inline]
  pub fn finish(self) -> flatbuffers::WIPOffset<Welcome<'a>> {
    let o = self.fbb_.end_table(self.start_);
    self.fbb_.required(o, Welcome::VT_ROLES,"roles");
    self.fbb_.required(o, Welcome::VT_REALM,"realm");
    self.fbb_.required(o, Welcome::VT_AUTHID,"authid");
    self.fbb_.required(o, Welcome::VT_AUTHROLE,"authrole");
    flatbuffers::WIPOffset::new(o.value())
  }
}

impl core::fmt::Debug for Welcome<'_> {
  fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
    let mut ds = f.debug_struct("Welcome");
      ds.field("roles", &self.roles());
      ds.field("session", &self.session());
      ds.field("realm", &self.realm());
      ds.field("authid", &self.authid());
      ds.field("authrole", &self.authrole());
      ds.field("authmethod", &self.authmethod());
      ds.field("authprovider", &self.authprovider());
      ds.field("authextra", &self.authextra());
      ds.field("resumed", &self.resumed());
      ds.field("resumable", &self.resumable());
      ds.field("resume_token", &self.resume_token());
      ds.finish()
  }
}
pub enum AbortOffset {}
#[derive(Copy, Clone, PartialEq)]

pub struct Abort<'a> {
  pub _tab: flatbuffers::Table<'a>,
}

impl<'a> flatbuffers::Follow<'a> for Abort<'a> {
  type Inner = Abort<'a>;
  #[inline]
  fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
    Self { _tab: flatbuffers::Table { buf, loc } }
  }
}

impl<'a> Abort<'a> {
  pub const VT_REASON: flatbuffers::VOffsetT = 4;
  pub const VT_MESSAGE: flatbuffers::VOffsetT = 6;

  #[inline]
  pub fn init_from_table(table: flatbuffers::Table<'a>) -> Self {
    Abort { _tab: table }
  }
  #[allow(unused_mut)]
  pub fn create<'bldr: 'args, 'args: 'mut_bldr, 'mut_bldr>(
    _fbb: &'mut_bldr mut flatbuffers::FlatBufferBuilder<'bldr>,
    args: &'args AbortArgs<'args>
  ) -> flatbuffers::WIPOffset<Abort<'bldr>> {
    let mut builder = AbortBuilder::new(_fbb);
    if let Some(x) = args.message { builder.add_message(x); }
    if let Some(x) = args.reason { builder.add_reason(x); }
    builder.finish()
  }


  #[inline]
  pub fn reason(&self) -> &'a str {
    self._tab.get::<flatbuffers::ForwardsUOffset<&str>>(Abort::VT_REASON, None).unwrap()
  }
  #[inline]
  pub fn message(&self) -> Option<&'a str> {
    self._tab.get::<flatbuffers::ForwardsUOffset<&str>>(Abort::VT_MESSAGE, None)
  }
}

impl flatbuffers::Verifiable for Abort<'_> {
  #[inline]
  fn run_verifier(
    v: &mut flatbuffers::Verifier, pos: usize
  ) -> Result<(), flatbuffers::InvalidFlatbuffer> {
    use self::flatbuffers::Verifiable;
    v.visit_table(pos)?
     .visit_field::<flatbuffers::ForwardsUOffset<&str>>("reason", Self::VT_REASON, true)?
     .visit_field::<flatbuffers::ForwardsUOffset<&str>>("message", Self::VT_MESSAGE, false)?
     .finish();
    Ok(())
  }
}
pub struct AbortArgs<'a> {
    pub reason: Option<flatbuffers::WIPOffset<&'a str>>,
    pub message: Option<flatbuffers::WIPOffset<&'a str>>,
}
impl<'a> Default for AbortArgs<'a> {
  #[inline]
  fn default() -> Self {
    AbortArgs {
      reason: None, // required field
      message: None,
    }
  }
}

pub struct AbortBuilder<'a: 'b, 'b> {
  fbb_: &'b mut flatbuffers::FlatBufferBuilder<'a>,
  start_: flatbuffers::WIPOffset<flatbuffers::TableUnfinishedWIPOffset>,
}
impl<'a: 'b, 'b> AbortBuilder<'a, 'b> {
  #[inline]
  pub fn add_reason(&mut self, reason: flatbuffers::WIPOffset<&'b  str>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<_>>(Abort::VT_REASON, reason);
  }
  #[inline]
  pub fn add_message(&mut self, message: flatbuffers::WIPOffset<&'b  str>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<_>>(Abort::VT_MESSAGE, message);
  }
  #[inline]
  pub fn new(_fbb: &'b mut flatbuffers::FlatBufferBuilder<'a>) -> AbortBuilder<'a, 'b> {
    let start = _fbb.start_table();
    AbortBuilder {
      fbb_: _fbb,
      start_: start,
    }
  }
  #[inline]
  pub fn finish(self) -> flatbuffers::WIPOffset<Abort<'a>> {
    let o = self.fbb_.end_table(self.start_);
    self.fbb_.required(o, Abort::VT_REASON,"reason");
    flatbuffers::WIPOffset::new(o.value())
  }
}

impl core::fmt::Debug for Abort<'_> {
  fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
    let mut ds = f.debug_struct("Abort");
      ds.field("reason", &self.reason());
      ds.field("message", &self.message());
      ds.finish()
  }
}
pub enum ChallengeOffset {}
#[derive(Copy, Clone, PartialEq)]

pub struct Challenge<'a> {
  pub _tab: flatbuffers::Table<'a>,
}

impl<'a> flatbuffers::Follow<'a> for Challenge<'a> {
  type Inner = Challenge<'a>;
  #[inline]
  fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
    Self { _tab: flatbuffers::Table { buf, loc } }
  }
}

impl<'a> Challenge<'a> {
  pub const VT_METHOD: flatbuffers::VOffsetT = 4;
  pub const VT_EXTRA: flatbuffers::VOffsetT = 6;

  #[inline]
  pub fn init_from_table(table: flatbuffers::Table<'a>) -> Self {
    Challenge { _tab: table }
  }
  #[allow(unused_mut)]
  pub fn create<'bldr: 'args, 'args: 'mut_bldr, 'mut_bldr>(
    _fbb: &'mut_bldr mut flatbuffers::FlatBufferBuilder<'bldr>,
    args: &'args ChallengeArgs<'args>
  ) -> flatbuffers::WIPOffset<Challenge<'bldr>> {
    let mut builder = ChallengeBuilder::new(_fbb);
    if let Some(x) = args.extra { builder.add_extra(x); }
    builder.add_method(args.method);
    builder.finish()
  }


  #[inline]
  pub fn method(&self) -> AuthMethod {
    self._tab.get::<AuthMethod>(Challenge::VT_METHOD, Some(AuthMethod::ANONYMOUS)).unwrap()
  }
  #[inline]
  pub fn extra(&self) -> Option<super::Map<'a>> {
    self._tab.get::<flatbuffers::ForwardsUOffset<super::Map>>(Challenge::VT_EXTRA, None)
  }
}

impl flatbuffers::Verifiable for Challenge<'_> {
  #[inline]
  fn run_verifier(
    v: &mut flatbuffers::Verifier, pos: usize
  ) -> Result<(), flatbuffers::InvalidFlatbuffer> {
    use self::flatbuffers::Verifiable;
    v.visit_table(pos)?
     .visit_field::<AuthMethod>("method", Self::VT_METHOD, false)?
     .visit_field::<flatbuffers::ForwardsUOffset<super::Map>>("extra", Self::VT_EXTRA, false)?
     .finish();
    Ok(())
  }
}
pub struct ChallengeArgs<'a> {
    pub method: AuthMethod,
    pub extra: Option<flatbuffers::WIPOffset<super::Map<'a>>>,
}
impl<'a> Default for ChallengeArgs<'a> {
  #[inline]
  fn default() -> Self {
    ChallengeArgs {
      method: AuthMethod::ANONYMOUS,
      extra: None,
    }
  }
}

pub struct ChallengeBuilder<'a: 'b, 'b> {
  fbb_: &'b mut flatbuffers::FlatBufferBuilder<'a>,
  start_: flatbuffers::WIPOffset<flatbuffers::TableUnfinishedWIPOffset>,
}
impl<'a: 'b, 'b> ChallengeBuilder<'a, 'b> {
  #[inline]
  pub fn add_method(&mut self, method: AuthMethod) {
    self.fbb_.push_slot::<AuthMethod>(Challenge::VT_METHOD, method, AuthMethod::ANONYMOUS);
  }
  #[inline]
  pub fn add_extra(&mut self, extra: flatbuffers::WIPOffset<super::Map<'b >>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<super::Map>>(Challenge::VT_EXTRA, extra);
  }
  #[inline]
  pub fn new(_fbb: &'b mut flatbuffers::FlatBufferBuilder<'a>) -> ChallengeBuilder<'a, 'b> {
    let start = _fbb.start_table();
    ChallengeBuilder {
      fbb_: _fbb,
      start_: start,
    }
  }
  #[inline]
  pub fn finish(self) -> flatbuffers::WIPOffset<Challenge<'a>> {
    let o = self.fbb_.end_table(self.start_);
    flatbuffers::WIPOffset::new(o.value())
  }
}

impl core::fmt::Debug for Challenge<'_> {
  fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
    let mut ds = f.debug_struct("Challenge");
      ds.field("method", &self.method());
      ds.field("extra", &self.extra());
      ds.finish()
  }
}
pub enum AuthenticateOffset {}
#[derive(Copy, Clone, PartialEq)]

pub struct Authenticate<'a> {
  pub _tab: flatbuffers::Table<'a>,
}

impl<'a> flatbuffers::Follow<'a> for Authenticate<'a> {
  type Inner = Authenticate<'a>;
  #[inline]
  fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
    Self { _tab: flatbuffers::Table { buf, loc } }
  }
}

impl<'a> Authenticate<'a> {
  pub const VT_SIGNATURE: flatbuffers::VOffsetT = 4;
  pub const VT_EXTRA: flatbuffers::VOffsetT = 6;

  #[inline]
  pub fn init_from_table(table: flatbuffers::Table<'a>) -> Self {
    Authenticate { _tab: table }
  }
  #[allow(unused_mut)]
  pub fn create<'bldr: 'args, 'args: 'mut_bldr, 'mut_bldr>(
    _fbb: &'mut_bldr mut flatbuffers::FlatBufferBuilder<'bldr>,
    args: &'args AuthenticateArgs<'args>
  ) -> flatbuffers::WIPOffset<Authenticate<'bldr>> {
    let mut builder = AuthenticateBuilder::new(_fbb);
    if let Some(x) = args.extra { builder.add_extra(x); }
    if let Some(x) = args.signature { builder.add_signature(x); }
    builder.finish()
  }


  #[inline]
  pub fn signature(&self) -> &'a str {
    self._tab.get::<flatbuffers::ForwardsUOffset<&str>>(Authenticate::VT_SIGNATURE, None).unwrap()
  }
  #[inline]
  pub fn extra(&self) -> Option<super::Map<'a>> {
    self._tab.get::<flatbuffers::ForwardsUOffset<super::Map>>(Authenticate::VT_EXTRA, None)
  }
}

impl flatbuffers::Verifiable for Authenticate<'_> {
  #[inline]
  fn run_verifier(
    v: &mut flatbuffers::Verifier, pos: usize
  ) -> Result<(), flatbuffers::InvalidFlatbuffer> {
    use self::flatbuffers::Verifiable;
    v.visit_table(pos)?
     .visit_field::<flatbuffers::ForwardsUOffset<&str>>("signature", Self::VT_SIGNATURE, true)?
     .visit_field::<flatbuffers::ForwardsUOffset<super::Map>>("extra", Self::VT_EXTRA, false)?
     .finish();
    Ok(())
  }
}
pub struct AuthenticateArgs<'a> {
    pub signature: Option<flatbuffers::WIPOffset<&'a str>>,
    pub extra: Option<flatbuffers::WIPOffset<super::Map<'a>>>,
}
impl<'a> Default for AuthenticateArgs<'a> {
  #[inline]
  fn default() -> Self {
    AuthenticateArgs {
      signature: None, // required field
      extra: None,
    }
  }
}

pub struct AuthenticateBuilder<'a: 'b, 'b> {
  fbb_: &'b mut flatbuffers::FlatBufferBuilder<'a>,
  start_: flatbuffers::WIPOffset<flatbuffers::TableUnfinishedWIPOffset>,
}
impl<'a: 'b, 'b> AuthenticateBuilder<'a, 'b> {
  #[inline]
  pub fn add_signature(&mut self, signature: flatbuffers::WIPOffset<&'b  str>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<_>>(Authenticate::VT_SIGNATURE, signature);
  }
  #[inline]
  pub fn add_extra(&mut self, extra: flatbuffers::WIPOffset<super::Map<'b >>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<super::Map>>(Authenticate::VT_EXTRA, extra);
  }
  #[inline]
  pub fn new(_fbb: &'b mut flatbuffers::FlatBufferBuilder<'a>) -> AuthenticateBuilder<'a, 'b> {
    let start = _fbb.start_table();
    AuthenticateBuilder {
      fbb_: _fbb,
      start_: start,
    }
  }
  #[inline]
  pub fn finish(self) -> flatbuffers::WIPOffset<Authenticate<'a>> {
    let o = self.fbb_.end_table(self.start_);
    self.fbb_.required(o, Authenticate::VT_SIGNATURE,"signature");
    flatbuffers::WIPOffset::new(o.value())
  }
}

impl core::fmt::Debug for Authenticate<'_> {
  fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
    let mut ds = f.debug_struct("Authenticate");
      ds.field("signature", &self.signature());
      ds.field("extra", &self.extra());
      ds.finish()
  }
}
pub enum GoodbyeOffset {}
#[derive(Copy, Clone, PartialEq)]

pub struct Goodbye<'a> {
  pub _tab: flatbuffers::Table<'a>,
}

impl<'a> flatbuffers::Follow<'a> for Goodbye<'a> {
  type Inner = Goodbye<'a>;
  #[inline]
  fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
    Self { _tab: flatbuffers::Table { buf, loc } }
  }
}

impl<'a> Goodbye<'a> {
  pub const VT_REASON: flatbuffers::VOffsetT = 4;
  pub const VT_MESSAGE: flatbuffers::VOffsetT = 6;
  pub const VT_RESUMABLE: flatbuffers::VOffsetT = 8;

  #[inline]
  pub fn init_from_table(table: flatbuffers::Table<'a>) -> Self {
    Goodbye { _tab: table }
  }
  #[allow(unused_mut)]
  pub fn create<'bldr: 'args, 'args: 'mut_bldr, 'mut_bldr>(
    _fbb: &'mut_bldr mut flatbuffers::FlatBufferBuilder<'bldr>,
    args: &'args GoodbyeArgs<'args>
  ) -> flatbuffers::WIPOffset<Goodbye<'bldr>> {
    let mut builder = GoodbyeBuilder::new(_fbb);
    if let Some(x) = args.message { builder.add_message(x); }
    if let Some(x) = args.reason { builder.add_reason(x); }
    builder.add_resumable(args.resumable);
    builder.finish()
  }


  #[inline]
  pub fn reason(&self) -> &'a str {
    self._tab.get::<flatbuffers::ForwardsUOffset<&str>>(Goodbye::VT_REASON, None).unwrap()
  }
  #[inline]
  pub fn message(&self) -> Option<&'a str> {
    self._tab.get::<flatbuffers::ForwardsUOffset<&str>>(Goodbye::VT_MESSAGE, None)
  }
  #[inline]
  pub fn resumable(&self) -> bool {
    self._tab.get::<bool>(Goodbye::VT_RESUMABLE, Some(false)).unwrap()
  }
}

impl flatbuffers::Verifiable for Goodbye<'_> {
  #[inline]
  fn run_verifier(
    v: &mut flatbuffers::Verifier, pos: usize
  ) -> Result<(), flatbuffers::InvalidFlatbuffer> {
    use self::flatbuffers::Verifiable;
    v.visit_table(pos)?
     .visit_field::<flatbuffers::ForwardsUOffset<&str>>("reason", Self::VT_REASON, true)?
     .visit_field::<flatbuffers::ForwardsUOffset<&str>>("message", Self::VT_MESSAGE, false)?
     .visit_field::<bool>("resumable", Self::VT_RESUMABLE, false)?
     .finish();
    Ok(())
  }
}
pub struct GoodbyeArgs<'a> {
    pub reason: Option<flatbuffers::WIPOffset<&'a str>>,
    pub message: Option<flatbuffers::WIPOffset<&'a str>>,
    pub resumable: bool,
}
impl<'a> Default for GoodbyeArgs<'a> {
  #[inline]
  fn default() -> Self {
    GoodbyeArgs {
      reason: None, // required field
      message: None,
      resumable: false,
    }
  }
}

pub struct GoodbyeBuilder<'a: 'b, 'b> {
  fbb_: &'b mut flatbuffers::FlatBufferBuilder<'a>,
  start_: flatbuffers::WIPOffset<flatbuffers::TableUnfinishedWIPOffset>,
}
impl<'a: 'b, 'b> GoodbyeBuilder<'a, 'b> {
  #[inline]
  pub fn add_reason(&mut self, reason: flatbuffers::WIPOffset<&'b  str>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<_>>(Goodbye::VT_REASON, reason);
  }
  #[inline]
  pub fn add_message(&mut self, message: flatbuffers::WIPOffset<&'b  str>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<_>>(Goodbye::VT_MESSAGE, message);
  }
  #[inline]
  pub fn add_resumable(&mut self, resumable: bool) {
    self.fbb_.push_slot::<bool>(Goodbye::VT_RESUMABLE, resumable, false);
  }
  #[inline]
  pub fn new(_fbb: &'b mut flatbuffers::FlatBufferBuilder<'a>) -> GoodbyeBuilder<'a, 'b> {
    let start = _fbb.start_table();
    GoodbyeBuilder {
      fbb_: _fbb,
      start_: start,
    }
  }
  #[inline]
  pub fn finish(self) -> flatbuffers::WIPOffset<Goodbye<'a>> {
    let o = self.fbb_.end_table(self.start_);
    self.fbb_.required(o, Goodbye::VT_REASON,"reason");
    flatbuffers::WIPOffset::new(o.value())
  }
}

impl core::fmt::Debug for Goodbye<'_> {
  fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
    let mut ds = f.debug_struct("Goodbye");
      ds.field("reason", &self.reason());
      ds.field("message", &self.message());
      ds.field("resumable", &self.resumable());
      ds.finish()
  }
}
pub enum ErrorOffset {}
#[derive(Copy, Clone, PartialEq)]

pub struct Error<'a> {
  pub _tab: flatbuffers::Table<'a>,
}

impl<'a> flatbuffers::Follow<'a> for Error<'a> {
  type Inner = Error<'a>;
  #[inline]
  fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
    Self { _tab: flatbuffers::Table { buf, loc } }
  }
}

impl<'a> Error<'a> {
  pub const VT_REQUEST_TYPE: flatbuffers::VOffsetT = 4;
  pub const VT_REQUEST: flatbuffers::VOffsetT = 6;
  pub const VT_ERROR: flatbuffers::VOffsetT = 8;
  pub const VT_PAYLOAD: flatbuffers::VOffsetT = 10;
  pub const VT_ENC_ALGO: flatbuffers::VOffsetT = 12;
  pub const VT_ENC_SERIALIZER: flatbuffers::VOffsetT = 14;
  pub const VT_ENC_KEY: flatbuffers::VOffsetT = 16;

  #[inline]
  pub fn init_from_table(table: flatbuffers::Table<'a>) -> Self {
    Error { _tab: table }
  }
  #[allow(unused_mut)]
  pub fn create<'bldr: 'args, 'args: 'mut_bldr, 'mut_bldr>(
    _fbb: &'mut_bldr mut flatbuffers::FlatBufferBuilder<'bldr>,
    args: &'args ErrorArgs<'args>
  ) -> flatbuffers::WIPOffset<Error<'bldr>> {
    let mut builder = ErrorBuilder::new(_fbb);
    builder.add_request(args.request);
    if let Some(x) = args.enc_key { builder.add_enc_key(x); }
    if let Some(x) = args.payload { builder.add_payload(x); }
    if let Some(x) = args.error { builder.add_error(x); }
    builder.add_request_type(args.request_type);
    builder.add_enc_serializer(args.enc_serializer);
    builder.add_enc_algo(args.enc_algo);
    builder.finish()
  }


  #[inline]
  pub fn request_type(&self) -> MessageType {
    self._tab.get::<MessageType>(Error::VT_REQUEST_TYPE, Some(MessageType::NULL)).unwrap()
  }
  #[inline]
  pub fn request(&self) -> u64 {
    self._tab.get::<u64>(Error::VT_REQUEST, Some(0)).unwrap()
  }
  #[inline]
  pub fn key_compare_less_than(&self, o: &Error) -> bool {
    self.request() < o.request()
  }

  #[inline]
  pub fn key_compare_with_value(&self, val: u64) -> ::core::cmp::Ordering {
    let key = self.request();
    key.cmp(&val)
  }
  #[inline]
  pub fn error(&self) -> &'a str {
    self._tab.get::<flatbuffers::ForwardsUOffset<&str>>(Error::VT_ERROR, None).unwrap()
  }
  #[inline]
  pub fn payload(&self) -> Option<&'a [u8]> {
    self._tab.get::<flatbuffers::ForwardsUOffset<flatbuffers::Vector<'a, u8>>>(Error::VT_PAYLOAD, None).map(|v| v.safe_slice())
  }
  #[inline]
  pub fn enc_algo(&self) -> Payload {
    self._tab.get::<Payload>(Error::VT_ENC_ALGO, Some(Payload::PLAIN)).unwrap()
  }
  #[inline]
  pub fn enc_serializer(&self) -> Serializer {
    self._tab.get::<Serializer>(Error::VT_ENC_SERIALIZER, Some(Serializer::TRANSPORT)).unwrap()
  }
  #[inline]
  pub fn enc_key(&self) -> Option<&'a [u8]> {
    self._tab.get::<flatbuffers::ForwardsUOffset<flatbuffers::Vector<'a, u8>>>(Error::VT_ENC_KEY, None).map(|v| v.safe_slice())
  }
}

impl flatbuffers::Verifiable for Error<'_> {
  #[inline]
  fn run_verifier(
    v: &mut flatbuffers::Verifier, pos: usize
  ) -> Result<(), flatbuffers::InvalidFlatbuffer> {
    use self::flatbuffers::Verifiable;
    v.visit_table(pos)?
     .visit_field::<MessageType>("request_type", Self::VT_REQUEST_TYPE, false)?
     .visit_field::<u64>("request", Self::VT_REQUEST, false)?
     .visit_field::<flatbuffers::ForwardsUOffset<&str>>("error", Self::VT_ERROR, true)?
     .visit_field::<flatbuffers::ForwardsUOffset<flatbuffers::Vector<'_, u8>>>("payload", Self::VT_PAYLOAD, false)?
     .visit_field::<Payload>("enc_algo", Self::VT_ENC_ALGO, false)?
     .visit_field::<Serializer>("enc_serializer", Self::VT_ENC_SERIALIZER, false)?
     .visit_field::<flatbuffers::ForwardsUOffset<flatbuffers::Vector<'_, u8>>>("enc_key", Self::VT_ENC_KEY, false)?
     .finish();
    Ok(())
  }
}
pub struct ErrorArgs<'a> {
    pub request_type: MessageType,
    pub request: u64,
    pub error: Option<flatbuffers::WIPOffset<&'a str>>,
    pub payload: Option<flatbuffers::WIPOffset<flatbuffers::Vector<'a, u8>>>,
    pub enc_algo: Payload,
    pub enc_serializer: Serializer,
    pub enc_key: Option<flatbuffers::WIPOffset<flatbuffers::Vector<'a, u8>>>,
}
impl<'a> Default for ErrorArgs<'a> {
  #[inline]
  fn default() -> Self {
    ErrorArgs {
      request_type: MessageType::NULL,
      request: 0,
      error: None, // required field
      payload: None,
      enc_algo: Payload::PLAIN,
      enc_serializer: Serializer::TRANSPORT,
      enc_key: None,
    }
  }
}

pub struct ErrorBuilder<'a: 'b, 'b> {
  fbb_: &'b mut flatbuffers::FlatBufferBuilder<'a>,
  start_: flatbuffers::WIPOffset<flatbuffers::TableUnfinishedWIPOffset>,
}
impl<'a: 'b, 'b> ErrorBuilder<'a, 'b> {
  #[inline]
  pub fn add_request_type(&mut self, request_type: MessageType) {
    self.fbb_.push_slot::<MessageType>(Error::VT_REQUEST_TYPE, request_type, MessageType::NULL);
  }
  #[inline]
  pub fn add_request(&mut self, request: u64) {
    self.fbb_.push_slot::<u64>(Error::VT_REQUEST, request, 0);
  }
  #[inline]
  pub fn add_error(&mut self, error: flatbuffers::WIPOffset<&'b  str>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<_>>(Error::VT_ERROR, error);
  }
  #[inline]
  pub fn add_payload(&mut self, payload: flatbuffers::WIPOffset<flatbuffers::Vector<'b , u8>>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<_>>(Error::VT_PAYLOAD, payload);
  }
  #[inline]
  pub fn add_enc_algo(&mut self, enc_algo: Payload) {
    self.fbb_.push_slot::<Payload>(Error::VT_ENC_ALGO, enc_algo, Payload::PLAIN);
  }
  #[inline]
  pub fn add_enc_serializer(&mut self, enc_serializer: Serializer) {
    self.fbb_.push_slot::<Serializer>(Error::VT_ENC_SERIALIZER, enc_serializer, Serializer::TRANSPORT);
  }
  #[inline]
  pub fn add_enc_key(&mut self, enc_key: flatbuffers::WIPOffset<flatbuffers::Vector<'b , u8>>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<_>>(Error::VT_ENC_KEY, enc_key);
  }
  #[inline]
  pub fn new(_fbb: &'b mut flatbuffers::FlatBufferBuilder<'a>) -> ErrorBuilder<'a, 'b> {
    let start = _fbb.start_table();
    ErrorBuilder {
      fbb_: _fbb,
      start_: start,
    }
  }
  #[inline]
  pub fn finish(self) -> flatbuffers::WIPOffset<Error<'a>> {
    let o = self.fbb_.end_table(self.start_);
    self.fbb_.required(o, Error::VT_ERROR,"error");
    flatbuffers::WIPOffset::new(o.value())
  }
}

impl core::fmt::Debug for Error<'_> {
  fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
    let mut ds = f.debug_struct("Error");
      ds.field("request_type", &self.request_type());
      ds.field("request", &self.request());
      ds.field("error", &self.error());
      ds.field("payload", &self.payload());
      ds.field("enc_algo", &self.enc_algo());
      ds.field("enc_serializer", &self.enc_serializer());
      ds.field("enc_key", &self.enc_key());
      ds.finish()
  }
}
}  // pub mod proto
}  // pub mod wamp

