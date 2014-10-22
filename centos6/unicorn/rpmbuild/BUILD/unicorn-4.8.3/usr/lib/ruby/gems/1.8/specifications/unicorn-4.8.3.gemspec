# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = %q{unicorn}
  s.version = "4.8.3"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["Unicorn hackers"]
  s.date = %q{2014-05-07}
  s.description = %q{\Unicorn is an HTTP server for Rack applications designed to only serve
fast clients on low-latency, high-bandwidth connections and take
advantage of features in Unix/Unix-like kernels.  Slow clients should
only be served by placing a reverse proxy capable of fully buffering
both the the request and response in between \Unicorn and slow clients.}
  s.email = %q{unicorn-public@bogomips.org}
  s.executables = ["unicorn", "unicorn_rails"]
  s.extensions = ["ext/unicorn_http/extconf.rb"]
  s.extra_rdoc_files = ["FAQ", "README", "TUNING", "PHILOSOPHY", "HACKING", "DESIGN", "CONTRIBUTORS", "LICENSE", "SIGNALS", "KNOWN_ISSUES", "TODO", "NEWS", "ChangeLog", "LATEST", "lib/unicorn.rb", "lib/unicorn/configurator.rb", "lib/unicorn/http_server.rb", "lib/unicorn/preread_input.rb", "lib/unicorn/stream_input.rb", "lib/unicorn/tee_input.rb", "lib/unicorn/util.rb", "lib/unicorn/oob_gc.rb", "lib/unicorn/worker.rb", "ISSUES", "Sandbox", "Links", "Application_Timeouts"]
  s.files = [".CHANGELOG.old", ".document", ".gitignore", ".mailmap", ".manifest", ".wrongdoc.yml", "Application_Timeouts", "CONTRIBUTORS", "COPYING", "ChangeLog", "DESIGN", "Documentation/.gitignore", "Documentation/GNUmakefile", "Documentation/unicorn.1.txt", "Documentation/unicorn_rails.1.txt", "FAQ", "GIT-VERSION-FILE", "GIT-VERSION-GEN", "GNUmakefile", "HACKING", "ISSUES", "KNOWN_ISSUES", "LATEST", "LICENSE", "Links", "NEWS", "PHILOSOPHY", "README", "Rakefile", "SIGNALS", "Sandbox", "TODO", "TUNING", "archive/.gitignore", "archive/slrnpull.conf", "bin/unicorn", "bin/unicorn_rails", "examples/big_app_gc.rb", "examples/echo.ru", "examples/git.ru", "examples/init.sh", "examples/logger_mp_safe.rb", "examples/logrotate.conf", "examples/nginx.conf", "examples/unicorn.conf.minimal.rb", "examples/unicorn.conf.rb", "ext/unicorn_http/CFLAGS", "ext/unicorn_http/c_util.h", "ext/unicorn_http/common_field_optimization.h", "ext/unicorn_http/ext_help.h", "ext/unicorn_http/extconf.rb", "ext/unicorn_http/global_variables.h", "ext/unicorn_http/httpdate.c", "ext/unicorn_http/unicorn_http.c", "ext/unicorn_http/unicorn_http.rl", "ext/unicorn_http/unicorn_http_common.rl", "lib/unicorn.rb", "lib/unicorn/app/exec_cgi.rb", "lib/unicorn/app/inetd.rb", "lib/unicorn/app/old_rails.rb", "lib/unicorn/app/old_rails/static.rb", "lib/unicorn/cgi_wrapper.rb", "lib/unicorn/configurator.rb", "lib/unicorn/const.rb", "lib/unicorn/http_request.rb", "lib/unicorn/http_response.rb", "lib/unicorn/http_server.rb", "lib/unicorn/launcher.rb", "lib/unicorn/oob_gc.rb", "lib/unicorn/preread_input.rb", "lib/unicorn/socket_helper.rb", "lib/unicorn/ssl_client.rb", "lib/unicorn/ssl_configurator.rb", "lib/unicorn/ssl_server.rb", "lib/unicorn/stream_input.rb", "lib/unicorn/tee_input.rb", "lib/unicorn/tmpio.rb", "lib/unicorn/util.rb", "lib/unicorn/version.rb", "lib/unicorn/worker.rb", "local.mk.sample", "man/man1/unicorn.1", "man/man1/unicorn_rails.1", "script/isolate_for_tests", "setup.rb", "t/.gitignore", "t/GNUmakefile", "t/README", "t/bin/content-md5-put", "t/bin/sha1sum.rb", "t/bin/unused_listen", "t/broken-app.ru", "t/detach.ru", "t/env.ru", "t/fails-rack-lint.ru", "t/heartbeat-timeout.ru", "t/hijack.ru", "t/listener_names.ru", "t/my-tap-lib.sh", "t/oob_gc.ru", "t/oob_gc_path.ru", "t/pid.ru", "t/preread_input.ru", "t/rack-input-tests.ru", "t/t0000-http-basic.sh", "t/t0001-reload-bad-config.sh", "t/t0002-config-conflict.sh", "t/t0002-parser-error.sh", "t/t0003-working_directory.sh", "t/t0004-heartbeat-timeout.sh", "t/t0004-working_directory_broken.sh", "t/t0005-working_directory_app.rb.sh", "t/t0006-reopen-logs.sh", "t/t0006.ru", "t/t0007-working_directory_no_embed_cli.sh", "t/t0008-back_out_of_upgrade.sh", "t/t0009-broken-app.sh", "t/t0009-winch_ttin.sh", "t/t0010-reap-logging.sh", "t/t0011-active-unix-socket.sh", "t/t0012-reload-empty-config.sh", "t/t0013-rewindable-input-false.sh", "t/t0013.ru", "t/t0014-rewindable-input-true.sh", "t/t0014.ru", "t/t0015-configurator-internals.sh", "t/t0016-trust-x-forwarded-false.sh", "t/t0017-trust-x-forwarded-true.sh", "t/t0018-write-on-close.sh", "t/t0019-max_header_len.sh", "t/t0020-at_exit-handler.sh", "t/t0021-process_detach.sh", "t/t0022-listener_names-preload_app.sh", "t/t0100-rack-input-tests.sh", "t/t0116-client_body_buffer_size.sh", "t/t0116.ru", "t/t0200-rack-hijack.sh", "t/t0300-no-default-middleware.sh", "t/t9000-preread-input.sh", "t/t9001-oob_gc.sh", "t/t9002-oob_gc-path.sh", "t/test-lib.sh", "t/write-on-close.ru", "test/aggregate.rb", "test/benchmark/README", "test/benchmark/dd.ru", "test/benchmark/stack.ru", "test/exec/README", "test/exec/test_exec.rb", "test/test_helper.rb", "test/unit/test_configurator.rb", "test/unit/test_droplet.rb", "test/unit/test_http_parser.rb", "test/unit/test_http_parser_ng.rb", "test/unit/test_http_parser_xftrust.rb", "test/unit/test_request.rb", "test/unit/test_response.rb", "test/unit/test_server.rb", "test/unit/test_signals.rb", "test/unit/test_sni_hostnames.rb", "test/unit/test_socket_helper.rb", "test/unit/test_stream_input.rb", "test/unit/test_tee_input.rb", "test/unit/test_upload.rb", "test/unit/test_util.rb", "unicorn.gemspec"]
  s.homepage = %q{http://unicorn.bogomips.org/}
  s.licenses = ["GPLv2+", "Ruby 1.8"]
  s.rdoc_options = ["-t", "Unicorn: Rack HTTP server for fast clients and Unix", "-W", "http://bogomips.org/unicorn.git/tree/%s"]
  s.require_paths = ["lib"]
  s.rubyforge_project = %q{mongrel}
  s.rubygems_version = %q{1.3.7}
  s.summary = %q{Rack HTTP server for fast clients and Unix}
  s.test_files = ["test/unit/test_configurator.rb", "test/unit/test_http_parser.rb", "test/unit/test_http_parser_ng.rb", "test/unit/test_http_parser_xftrust.rb", "test/unit/test_request.rb", "test/unit/test_response.rb", "test/unit/test_server.rb", "test/unit/test_sni_hostnames.rb", "test/unit/test_util.rb"]

  if s.respond_to? :specification_version then
    current_version = Gem::Specification::CURRENT_SPECIFICATION_VERSION
    s.specification_version = 4

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_runtime_dependency(%q<rack>, [">= 0"])
      s.add_runtime_dependency(%q<kgio>, ["~> 2.6"])
      s.add_runtime_dependency(%q<raindrops>, ["~> 0.7"])
      s.add_development_dependency(%q<isolate>, ["~> 3.2"])
      s.add_development_dependency(%q<wrongdoc>, ["~> 1.8"])
    else
      s.add_dependency(%q<rack>, [">= 0"])
      s.add_dependency(%q<kgio>, ["~> 2.6"])
      s.add_dependency(%q<raindrops>, ["~> 0.7"])
      s.add_dependency(%q<isolate>, ["~> 3.2"])
      s.add_dependency(%q<wrongdoc>, ["~> 1.8"])
    end
  else
    s.add_dependency(%q<rack>, [">= 0"])
    s.add_dependency(%q<kgio>, ["~> 2.6"])
    s.add_dependency(%q<raindrops>, ["~> 0.7"])
    s.add_dependency(%q<isolate>, ["~> 3.2"])
    s.add_dependency(%q<wrongdoc>, ["~> 1.8"])
  end
end
