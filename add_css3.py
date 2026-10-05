import re

with open("ui/cloudbrains/create/index.html", "r", encoding="utf-8") as f:
    html = f.read()

css = """
/* ============================================================
   CREATE TASK FORM - DARK MODE TWEAKS
   ============================================================ */
.create-form-wrap {
  padding-top: 20px;
}
.ai-task-create-global-c {
  color: var(--text);
}
.ai-task-create-global-c .create-task-warp {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 24px;
}
.ai-task-create-global-c .area-l-title {
  display: none; /* Hide old breadcrumb, we use new pagehead */
}
.ai-task-create-global-c .main-title {
  color: var(--text);
  font-weight: 600;
  font-size: 15px;
  margin-bottom: 24px;
  border-bottom: 1px solid var(--border-2);
  padding-bottom: 12px;
}
.ai-task-create-global-c .form-row {
  display: flex;
  margin-bottom: 24px;
  align-items: flex-start;
}
.ai-task-create-global-c .form-row .left-area {
  display: flex;
  flex: 1;
}
.ai-task-create-global-c .form-row .title {
  width: 130px;
  color: var(--text-dim);
  font-size: 13.5px;
  flex: none;
  display: flex;
  align-items: flex-start;
  padding-top: 8px;
}
.ai-task-create-global-c .form-row .title .required::before {
  content: "*";
  color: var(--red);
  margin-right: 4px;
}
.ai-task-create-global-c .form-row .content {
  flex: 1;
}
.ai-task-create-global-c .task-items-c {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin-bottom: 20px;
}
.ai-task-create-global-c .task-item {
  border: 1px solid var(--border-2);
  background: var(--bg-2);
  padding: 16px 20px;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.2s;
  flex: 1;
  min-width: 140px;
  max-width: 180px;
}
.ai-task-create-global-c .task-item:hover {
  border-color: var(--accent);
}
.ai-task-create-global-c .task-item.focus {
  border-color: var(--accent);
  background: rgba(0, 229, 199, 0.08);
}
.ai-task-create-global-c .task-item-name {
  color: var(--text);
  font-weight: 500;
  margin-bottom: 6px;
  font-size: 14px;
}
.ai-task-create-global-c .task-item-desc {
  color: var(--text-mute);
  font-size: 12px;
}
.ai-task-create-global-c .tips {
  color: var(--text-mute);
  font-size: 12px;
  margin-top: 6px;
}
.ai-task-create-global-c .tips a {
  color: var(--accent);
  text-decoration: none;
}
.ai-task-create-global-c .tips a:hover {
  text-decoration: underline;
}
.ai-task-create-global-c .list {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}
.ai-task-create-global-c .list .item {
  padding: 6px 14px;
  border-radius: 20px;
  border: 1px solid var(--border-2);
  background: var(--bg-2);
  color: var(--text-dim);
  cursor: pointer;
  transition: .2s;
  font-size: 13px;
}
.ai-task-create-global-c .list .item:hover {
  border-color: var(--accent);
  color: var(--accent);
}
.ai-task-create-global-c .list .item.focus {
  border-color: var(--accent);
  background: rgba(0, 229, 199, 0.08);
  color: var(--accent);
}
.ai-task-create-global-c .el-input__inner,
.ai-task-create-global-c .el-textarea__inner {
  width: 100%;
  max-width: 400px;
  background: var(--bg-2);
  border: 1px solid var(--border-2);
  border-radius: 6px;
  padding: 8px 12px;
  color: var(--text);
  outline: none;
  font-family: var(--f-body);
  font-size: 13px;
  transition: border-color 0.2s;
}
.ai-task-create-global-c .el-textarea__inner {
  resize: vertical;
  min-height: 80px;
}
.ai-task-create-global-c .el-input__inner:focus,
.ai-task-create-global-c .el-textarea__inner:focus {
  border-color: var(--accent);
}
.ai-task-create-global-c .el-input__inner[readonly] {
  background: var(--bg);
  color: var(--text-mute);
  cursor: pointer;
}
.ai-task-create-global-c .spec-info {
  background: var(--bg-2);
  border: 1px solid var(--border-2);
  border-radius: 8px;
  padding: 12px;
  max-width: 500px;
}
.ai-task-create-global-c .spec-sel-icon {
  margin-right: 8px;
}
.ai-task-create-global-c .NPU_icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 18px;
  height: 18px;
  background: var(--accent);
  color: #000;
  border-radius: 4px;
  font-size: 10px;
  font-weight: bold;
}
.ai-task-create-global-c .spec-sel-point {
  color: var(--accent);
  font-size: 12px;
}
.ai-task-create-global-c .self-point-info {
  margin-top: 10px;
  font-size: 12px;
  color: var(--text-dim);
}
.ai-task-create-global-c .btn-select,
.ai-task-create-global-c .model-item-placeholder {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  padding: 8px 16px;
  background: var(--surface-2);
  border: 1px dashed var(--border-2);
  border-radius: 6px;
  color: var(--text);
  cursor: pointer;
  transition: .2s;
  font-size: 13px;
}
.ai-task-create-global-c .btn-select:hover,
.ai-task-create-global-c .model-item-placeholder:hover {
  border-color: var(--accent);
  color: var(--accent);
}
.ai-task-create-global-c .model-item-placeholder i {
  margin-right: 6px;
}
.ai-task-create-global-c .form-right {
  display: block;
  width: 320px;
  flex: none;
}
/* Flex layout for form content */
.ai-task-create-global-c .form-content {
  display: flex;
  gap: 40px;
}
.ai-task-create-global-c .form-left {
  flex: 1;
}
.ai-task-create-global-c .form-right-content {
  background: var(--surface-2);
  border: 1px solid var(--border-2);
  border-radius: 8px;
  padding: 16px;
}
.ai-task-create-global-c .form-right .title {
  color: var(--text-dim);
  font-size: 13px;
  margin-bottom: 12px;
}
.ai-task-create-global-c .form-right .code-c {
  background: var(--bg);
  padding: 12px;
  border-radius: 6px;
  border: 1px solid var(--border-2);
}
.ai-task-create-global-c .form-right pre {
  font-family: var(--f-mono);
  font-size: 12px;
  color: var(--text-dim);
  margin: 0;
  white-space: pre-wrap;
}
.ai-task-create-global-c .form-right .copy-btn {
  text-align: right;
  margin-top: 8px;
}
.ai-task-create-global-c .form-right .copy-btn a {
  color: var(--accent);
  font-size: 12px;
  text-decoration: none;
}
.ai-task-create-global-c .line {
  height: 1px;
  background: var(--border-2);
  margin: 30px 0;
}
/* Radio buttons */
.ai-task-create-global-c .el-radio-group {
  display: flex;
  gap: 16px;
  padding-top: 6px;
}
.ai-task-create-global-c .el-radio {
  display: flex;
  align-items: center;
  gap: 6px;
  color: var(--text-dim);
  cursor: pointer;
  font-size: 13px;
}
.ai-task-create-global-c .el-radio__inner {
  width: 14px;
  height: 14px;
  border: 1px solid var(--border-2);
  border-radius: 50%;
  display: inline-block;
  position: relative;
}
.ai-task-create-global-c .el-radio.is-checked .el-radio__inner {
  border-color: var(--accent);
  background: var(--bg);
}
.ai-task-create-global-c .el-radio.is-checked .el-radio__inner::after {
  content: "";
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--accent);
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.ai-task-create-global-c .el-checkbox {
  display: flex;
  align-items: center;
  gap: 6px;
  color: var(--text-dim);
  cursor: pointer;
  font-size: 13px;
}
.ai-task-create-global-c .el-checkbox__inner {
  width: 14px;
  height: 14px;
  border: 1px solid var(--border-2);
  border-radius: 3px;
  display: inline-block;
  position: relative;
}
.ai-task-create-global-c .right-area {
  padding-left: 10px;
}
.ai-task-create-global-c .resource-descr {
  font-size: 12px;
  padding-top: 8px;
}
.ai-task-create-global-c .resource-descr a {
  color: var(--accent-3);
  text-decoration: none;
}
.ai-task-create-global-c .wait-count-c {
  color: var(--accent-2);
  display: inline-flex;
  align-items: center;
  gap: 4px;
}
/* Ensure form wrapper inputs are reset */
.ai-task-create-global-c .el-input__prefix,
.ai-task-create-global-c .el-input__suffix {
  display: flex;
  align-items: center;
  height: 100%;
  padding: 0 8px;
}
.ai-task-create-global-c .el-input {
  position: relative;
  display: flex;
  align-items: center;
}
.ai-task-create-global-c .el-input--prefix .el-input__inner {
  padding-left: 100px;
}
.ai-task-create-global-c .el-input--suffix .el-input__inner {
  padding-right: 30px;
}
.ai-task-create-global-c .el-input__prefix {
  position: absolute;
  left: 0;
  top: 0;
}
.ai-task-create-global-c .el-input__suffix {
  position: absolute;
  right: 0;
  top: 0;
}

/* Base Dialog Hide */
.base-dlg, .el-dialog__wrapper, .el-select-dropdown {
  display: none;
}

/* Hide some messy elements */
.el-radio__original, .el-checkbox__original {
  display: none;
}
.ai-task-create-global-c .btn-select .el-icon-plus::before {
  content: "+ ";
}

/* Specific overrides for cleaner dark mode UI */
.hljs-keyword { color: var(--magenta); }
.hljs-comment { color: var(--text-mute); }
"""

html = html.replace('</style>', css + '\n</style>')

with open("ui/cloudbrains/create/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("CSS injected successfully.")
