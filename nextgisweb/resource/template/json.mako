<%inherit file='nextgisweb:templates/obj.mako' />

<% from json import dumps %>

<script type="text/javascript">
    require(["ngw/form/CodeMirror", "dojo/domReady!"], function (CodeMirror) {
        var cm = new CodeMirror({autoHeight: true, mode: "javascript", lineNumbers: true, readonly: true}).placeAt('content');
        cm.set("value", ${dumps(dumps(objjson, ensure_ascii=False, indent=4)) | n});
    });
</script>

<div id="content">

</div>
