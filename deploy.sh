#!/bin/bash
# Script para desplegar MkDocs sin problemas
# Uso: ./deploy.sh

echo "🔄 Sincronizando rama gh-pages..."
git fetch origin gh-pages

echo "🚀 Desplegando documentación..."
mkdocs gh-deploy

echo "✅ Despliegue completado!"
echo "📖 Documentación disponible en: https://fjavier-hernandez.github.io/ral/"
