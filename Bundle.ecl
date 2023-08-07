IMPORT Std;
EXPORT Bundle := MODULE(Std.BundleBase)
  EXPORT Name := 'ChatGPT';
  EXPORT Description := 'Generalized AI Bundle';
  EXPORT Authors := ['HPCCSystems'];
  EXPORT License := 'http://www.apache.org/licenses/LICENSE-2.0';
  EXPORT Copyright := 'Copyright (C) 2023 HPCC Systems®';
  EXPORT DependsOn := ['openai'];
  EXPORT Version := '1.0.0';
  EXPORT PlatformVersion := '9.0.4';
END;