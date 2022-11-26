module github.com/longhorn/longhorn-instance-manager

go 1.18

require (
	github.com/RoaringBitmap/roaring v0.4.18
	github.com/golang/protobuf v1.5.2
	github.com/google/uuid v1.3.0
	github.com/longhorn/backupstore v0.0.0-20221114044558-19f4902cd4fd
	github.com/longhorn/longhorn-engine v1.3.2
	github.com/pkg/errors v0.9.1
	github.com/sirupsen/logrus v1.9.0
	github.com/uptrace/opentelemetry-go-extra/otellogrus v0.1.17
	github.com/urfave/cli v1.22.10
	go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc v0.36.4
	go.opentelemetry.io/otel v1.11.1
	go.opentelemetry.io/otel/exporters/otlp/otlptrace v1.11.1
	go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc v1.11.1
	go.opentelemetry.io/otel/metric v0.33.0
	go.opentelemetry.io/otel/sdk v1.11.1
	golang.org/x/net v0.2.0
	google.golang.org/grpc v1.51.0
	gopkg.in/check.v1 v1.0.0-20180628173108-788fd7840127
)

require (
	cloud.google.com/go/compute/metadata v0.2.1 // indirect
	github.com/aws/aws-sdk-go v1.44.145 // indirect
	github.com/c9s/goprocinfo v0.0.0-20210130143923-c95fcf8c64a8 // indirect
	github.com/cenkalti/backoff/v4 v4.1.3 // indirect
	github.com/cpuguy83/go-md2man/v2 v2.0.2 // indirect
	github.com/felixge/httpsnoop v1.0.3 // indirect
	github.com/glycerine/go-unsnap-stream v0.0.0-20210130063903-47dfef350d96 // indirect
	github.com/go-logr/logr v1.2.3 // indirect
	github.com/go-logr/stdr v1.2.2 // indirect
	github.com/golang/snappy v0.0.1 // indirect
	github.com/gorilla/handlers v1.5.1 // indirect
	github.com/grpc-ecosystem/grpc-gateway/v2 v2.7.0 // indirect
	github.com/honestbee/jobq v1.0.2 // indirect
	github.com/jmespath/go-jmespath v0.4.0 // indirect
	github.com/kr/pretty v0.1.0 // indirect
	github.com/kr/text v0.1.0 // indirect
	github.com/longhorn/go-iscsi-helper v0.0.0-20221109111031-ebff48f3632a // indirect
	github.com/longhorn/sparse-tools v0.0.0-20221114062818-310a74664931 // indirect
	github.com/mschoch/smat v0.0.0-20160514031455-90eadee771ae // indirect
	github.com/philhofer/fwd v1.0.0 // indirect
	github.com/rancher/go-fibmap v0.0.0-20160418233256-5fc9f8c1ed47 // indirect
	github.com/russross/blackfriday/v2 v2.1.0 // indirect
	github.com/tinylib/msgp v1.1.1-0.20190612170807-0573788bc2a8 // indirect
	github.com/uptrace/opentelemetry-go-extra/otelutil v0.1.17 // indirect
	github.com/willf/bitset v1.1.10 // indirect
	go.opentelemetry.io/otel/exporters/otlp/internal/retry v1.11.1 // indirect
	go.opentelemetry.io/otel/trace v1.11.1 // indirect
	go.opentelemetry.io/proto/otlp v0.19.0 // indirect
	golang.org/x/sys v0.2.0 // indirect
	golang.org/x/text v0.4.0 // indirect
	google.golang.org/genproto v0.0.0-20221118155620-16455021b5e6 // indirect
	google.golang.org/protobuf v1.28.1 // indirect
)

replace golang.org/x/text v0.3.2 => golang.org/x/text v0.3.3

replace github.com/longhorn/longhorn-engine => github.com/jaysonsantos/longhorn-engine v1.3.3-0.20221028061608-5cc29e32a5fb
