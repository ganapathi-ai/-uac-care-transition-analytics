# 🚀 Deploy to Streamlit Cloud (FREE)

## Step-by-Step Deployment Guide

### **Step 1: Create GitHub Repository**

1. Go to https://github.com/new
2. Repository name: `uac-care-transition-analytics`
3. Set to **Public**
4. Click "Create repository"

### **Step 2: Push Your Code to GitHub**

Open terminal in your project folder and run:

```bash
cd c:\Users\lenovo\Downloads\UAC_Care_Transition

git init
git add .
git commit -m "Initial commit - UAC Care Transition Analytics"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/uac-care-transition-analytics.git
git push -u origin main
```

**Replace `YOUR_USERNAME` with your GitHub username!**

### **Step 3: Deploy on Streamlit Cloud**

1. Go to https://share.streamlit.io/
2. Click **"New app"**
3. Connect your GitHub account (if not already)
4. Select:
   - **Repository:** `YOUR_USERNAME/uac-care-transition-analytics`
   - **Branch:** `main`
   - **Main file path:** `app.py`
5. Click **"Deploy!"**

### **Step 4: Get Your Public URL**

After 2-3 minutes, you'll get a URL like:
```
https://YOUR_USERNAME-uac-care-transition-analytics.streamlit.app
```

**That's your permanent public URL!** 🌍

---

## ⚡ Quick Alternative (If No GitHub Account)

### Use Streamlit Community Cloud Directly:

1. Create account at https://share.streamlit.io/
2. Upload your project as ZIP
3. Deploy directly

---

## 📋 Pre-Deployment Checklist

✅ All files in place:
- `app.py`
- `requirements.txt`
- `data/uac_metrics_processed.csv`
- `README.md`

✅ Requirements.txt is correct
✅ Data files are in `data/` folder
✅ App runs locally without errors

---

## 🔧 Troubleshooting

**Issue:** "Module not found"
- **Fix:** Check `requirements.txt` has all dependencies

**Issue:** "File not found"
- **Fix:** Ensure data files are in `data/` folder in GitHub repo

**Issue:** "App won't start"
- **Fix:** Test locally first with `streamlit run app.py`

---

## 💡 Benefits of Streamlit Cloud

✅ **FREE** hosting
✅ **Automatic updates** when you push to GitHub
✅ **HTTPS** by default
✅ **No server management**
✅ **Permanent URL**
✅ **Share with anyone**

---

## 🎯 Your Final Public URL Will Be:

```
https://YOUR_USERNAME-uac-care-transition-analytics.streamlit.app
```

**Share this URL with stakeholders, professors, or anyone!** 🚀

---

## 📞 Need Help?

- Streamlit Docs: https://docs.streamlit.io/streamlit-community-cloud
- GitHub Guide: https://docs.github.com/en/get-started/quickstart

**Deployment time: 5-10 minutes total!** ⚡
