{{/*
App name
*/}}
{{- define "calculator-app.name" -}}
{{- .Release.Name }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "calculator-app.labels" -}}
app: {{ include "calculator-app.name" . }}
release: {{ .Release.Name }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "calculator-app.selectorLabels" -}}
app: {{ include "calculator-app.name" . }}
{{- end }}
